from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPostView,CreateProfilePageView,FriendView,ShowProfilePageView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('friends/', FriendView.as_view(), name='friends'),
    path('search', views.search, name='search'),
    path('like-post', views.like_post, name='like-post'),
    path('follow', views.follow, name='follow'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
