from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Post, Category, Tag
from .forms import CommentForm, ContactForm, SearchForm


def home(request):
    pinned_post = Post.objects.filter(status='published', is_pinned=True).first()
    posts = Post.objects.filter(status='published').exclude(
        pk=pinned_post.pk if pinned_post else 0
    )[:6]
    categories = Category.objects.all()

    context = {
        'pinned_post': pinned_post,
        'posts': posts,
        'categories': categories,
        'page_title': settings.BLOG_TITLE,
        'meta_description': settings.BLOG_DESCRIPTION,
    }
    return render(request, 'blog/home.html', context)


def post_list(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts,
        'page_title': f"Maqolalar — {settings.BLOG_TITLE}",
        'meta_description': "Barcha nashr etilgan maqolalar ro'yxati",
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')

    # View count
    session_key = f'viewed_post_{post.pk}'
    if not request.session.get(session_key, False):
        post.view_count += 1
        post.save(update_fields=['view_count'])
        request.session[session_key] = True

    # Previous and next posts
    prev_post = Post.objects.filter(
        status='published', created_at__lt=post.created_at
    ).first()
    next_post = Post.objects.filter(
        status='published', created_at__gt=post.created_at
    ).order_by('created_at').first()

    # Comments
    comments = post.approved_comments()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Izohingiz yuborildi! Admin tasdiqlashini kuting.")
            return redirect(post.get_absolute_url())

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments': comments,
        'comment_form': comment_form,
        'page_title': f"{post.title} — {settings.BLOG_TITLE}",
        'meta_description': (post.excerpt or '')[:160],
    }
    return render(request, 'blog/post_detail.html', context)


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(status='published', category=category)
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'category': category,
        'posts': posts,
        'page_title': f"{category.name} — {settings.BLOG_TITLE}",
        'meta_description': category.description or f"{category.name} kategoriyasidagi maqolalar",
    }
    return render(request, 'blog/category.html', context)


def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(status='published', tags=tag)
    paginator = Paginator(posts, settings.POSTS_PER_PAGE)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'tag': tag,
        'posts': posts,
        'page_title': f"#{tag.name} — {settings.BLOG_TITLE}",
        'meta_description': f"'{tag.name}' tegi bo'yicha maqolalar",
    }
    return render(request, 'blog/tag.html', context)


def search_view(request):
    form = SearchForm(request.GET or None)
    results = []
    query = ''

    if form.is_valid():
        query = form.cleaned_data['q']
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status='published'
        )

    paginator = Paginator(results, settings.POSTS_PER_PAGE)
    page = request.GET.get('page')
    results = paginator.get_page(page)

    context = {
        'form': form,
        'results': results,
        'query': query,
        'page_title': f"Qidiruv: {query} — {settings.BLOG_TITLE}" if query else f"Qidiruv — {settings.BLOG_TITLE}",
        'meta_description': f"'{query}' bo'yicha qidiruv natijalari" if query else "Blog bo'yicha qidiruv",
    }
    return render(request, 'blog/search.html', context)


def about_view(request):
    context = {
        'page_title': f"Men haqimda — {settings.BLOG_TITLE}",
        'meta_description': "Blog muallifi haqida ma'lumot",
    }
    return render(request, 'blog/about.html', context)


def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Kimdan: {name}\nEmail: {email}\n\n{message}"

            try:
                send_mail(
                    f"Blog aloqa formasi: {subject}",
                    full_message,
                    email,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, "Xabaringiz yuborildi! Tez orada javob beramiz.")
            return redirect('blog:contact')

    context = {
        'form': form,
        'page_title': f"Aloqa — {settings.BLOG_TITLE}",
        'meta_description': "Biz bilan bog'lanish uchun aloqa sahifasi",
    }
    return render(request, 'blog/contact.html', context)


def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_500(request):
    return render(request, 'errors/500.html', status=500)
