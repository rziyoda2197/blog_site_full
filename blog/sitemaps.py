from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Category.objects.all()


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['blog:home', 'blog:post_list', 'blog:about', 'blog:contact']

    def location(self, item):
        return reverse(item)
