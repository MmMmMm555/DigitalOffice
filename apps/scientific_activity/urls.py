from django.urls import path

from apps.scientific_activity.api_endpoints.article_crud.views import (
    ArticleCreateAPIView, ArticleListAPIView,
    ArticleUpdateAPIView, ArticleDetailAPIView,
    ArticleDeleteAPIView,)
from apps.scientific_activity.api_endpoints.book_crud.views import (
    BookCreateAPIView, BookListAPIView,
    BookUpdateAPIView, BookDetailAPIView,
    BookDeleteAPIView,)
from apps.scientific_activity.api_endpoints.article_images_api.views import (
    ArticleImageCreateApiView, ArticleImageListApiView,)
from apps.scientific_activity.api_endpoints.book_images_api.views import (
    BookImageCreateApiView, BookImageListApiView,)

urlpatterns = [
    # article apis
    path('article/create', ArticleCreateAPIView.as_view(), name='create'),
    path('article/list', ArticleListAPIView.as_view(), name='list'),
    path('article/update/<int:pk>', ArticleUpdateAPIView.as_view(), name='update'),
    path('article/detail/<int:pk>', ArticleDetailAPIView.as_view(), name='detail'),
    path('article/delete/<int:pk>', ArticleDeleteAPIView.as_view(), name='delete'),

    # article images apis
    path('article_image/create', ArticleImageCreateApiView.as_view(), name='image_create'),
    path('article_image/list/', ArticleImageListApiView.as_view(), name='image_list'),


    # book apis
    path('book/create', BookCreateAPIView.as_view(), name='create'),
    path('book/list', BookListAPIView.as_view(), name='list'),
    path('book/update/<int:pk>', BookUpdateAPIView.as_view(), name='update'),
    path('book/detail/<int:pk>', BookDetailAPIView.as_view(), name='detail'),
    path('book/delete/<int:pk>', BookDeleteAPIView.as_view(), name='delete'),

    # # book images apis
    path('book_image/create', BookImageCreateApiView.as_view(), name='image_create'),
    path('book_image/list/', BookImageListApiView.as_view(), name='image_list'),
]
