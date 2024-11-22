from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # slug after the colon gets its value from the URL path to post_detail, in index.html
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]