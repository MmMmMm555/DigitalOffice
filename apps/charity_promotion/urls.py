from django.urls import path
from apps.charity_promotion.api_endpoints.charity import views
from apps.charity_promotion.api_endpoints.images_api.views import ImageCreateApiView, ImageListApiView 

urlpatterns = [
    # charity promotion apis
    path('create', views.CharityPromotionCreateView.as_view(), name='charity_create'),
    path('list/', views.CharityPromotionListView.as_view(), name='charity_list'),
    path('detail/<int:pk>', views.CharityPromotionDetailView.as_view(), name='charity_detail'),
    path('update/<int:pk>', views.CharityPromotionUpdateView.as_view(), name='charity_update'),
    path('delete/<int:pk>', views.CharityPromotionDeleteView.as_view(), name='charity_delete'),
    # images apis
    path('image/create', ImageCreateApiView.as_view(), name='image_create'),
    path('image/list/', ImageListApiView.as_view(), name='image_list'),
]
