
from django.urls import path
from .views import AddPostView, ArticleDetailView, DeletePostView, HomeView , UpdatePostView

urlpatterns = [
    # path('',views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('<int:pk>/remove', DeletePostView.as_view(), name='delate_post'),
]
