from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('tag/<slug:slug>/', views.tag_view, name='tag'),
    path('search/', views.search_view, name='search'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
