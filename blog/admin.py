from django.contrib import admin
from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'post_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('name', 'email', 'body', 'created_at')
    fields = ('name', 'email', 'body', 'is_approved', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_pinned', 'view_count', 'comment_count', 'created_at')
    list_filter = ('status', 'category', 'is_pinned', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'is_pinned')
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
    readonly_fields = ('view_count', 'created_at', 'updated_at')
    inlines = [CommentInline]

    fieldsets = (
        ('Asosiy', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'image')
        }),
        ('Kategoriya va Teglar', {
            'fields': ('category', 'tags')
        }),
        ('Holati', {
            'fields': ('status', 'is_pinned')
        }),
        ('Statistika', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    list_editable = ('is_approved',)
    actions = ['approve_comments', 'reject_comments']

    @admin.action(description="Tanlangan izohlarni tasdiqlash")
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    @admin.action(description="Tanlangan izohlarni rad etish")
    def reject_comments(self, request, queryset):
        queryset.update(is_approved=False)
