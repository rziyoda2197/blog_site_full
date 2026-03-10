from .models import Category, Tag, Post


def sidebar_context(request):
    """Global context for sidebar: popular posts, categories, tags."""
    return {
        'sidebar_categories': Category.objects.all()[:10],
        'sidebar_tags': Tag.objects.all()[:20],
        'sidebar_popular_posts': Post.objects.filter(
            status='published'
        ).order_by('-view_count')[:5],
    }
