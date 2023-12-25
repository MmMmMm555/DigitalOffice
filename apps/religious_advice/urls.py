from django.urls import path

from apps.religious_advice.api_endpoints.religious_advice_crud import views


urlpatterns = [
    # religiousAdvice apis
    path('create/', views.ReligiousAdviceCreateAPIView.as_view(),
         name='religiousAdvice_create'),
    path('list/', views.ReligiousAdviceListAPIView.as_view(),
         name='religiousAdvice_list'),
    path('detail/<int:pk>/', views.ReligiousAdviceDetailAPIView.as_view(),
         name='religiousAdvice_detail'),
    path('update/<int:pk>/', views.ReligiousAdviceUpdateAPIView.as_view(),
         name='religiousAdvice_update'),
    path('delete/<int:pk>', views.ReligiousAdviceDeleteAPIView.as_view(),
         name='religiousAdvice_delete'),
]
