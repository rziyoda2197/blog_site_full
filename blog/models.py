from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import math


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    def post_count(self):
        return self.posts.filter(status='published').count()


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Teg nomi")
    slug = models.SlugField(unique=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})

    def post_count(self):
        return self.posts.filter(status='published').count()


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Qoralama'),
        ('published', 'Nashr etilgan'),
    )

    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Asosiy matn")
    excerpt = models.TextField(verbose_name="Qisqa tavsif", help_text="Maqolalar ro'yxatida ko'rsatiladi")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name="Kategoriya")
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name="Teglar")
    image = models.ImageField(upload_to='posts/%Y/%m/', blank=True, null=True, verbose_name="Muqova rasmi")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Holati")
    is_pinned = models.BooleanField(default=False, verbose_name="Pinlangan")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def reading_time(self):
        word_count = len(self.content.split())
        minutes = math.ceil(word_count / 200)
        return max(1, minutes)

    def approved_comments(self):
        return self.comments.filter(is_approved=True)

    def comment_count(self):
        return self.approved_comments().count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Maqola")
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    body = models.TextField(verbose_name="Izoh matni")
    is_approved = models.BooleanField(default=False, verbose_name="Tasdiqlangan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yozilgan vaqt")

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.name} — {self.post.title[:30]}"
