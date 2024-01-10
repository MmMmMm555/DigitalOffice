from django.urls import path

from apps.individual_conversations.api_endpoints.individual_conversation_crud import views
from apps.individual_conversations.api_endpoints.images_crud.views import ImageCreateApiView, ImageListApiView

urlpatterns = [
    # individual conversation apis
    path('create', views.IndividualConversationCreateView.as_view(), name='create'),
    path('list/', views.IndividualConversationListView.as_view(), name='list'),
    path('detail/<int:pk>',
         views.IndividualConversationDetailView.as_view(), name='detail'),
    path('update<int:pk>',
         views.IndividualConversationUpdateView.as_view(), name='update'),
    path('delete<int:pk>',
         views.IndividualConversationDeleteView.as_view(), name='delete'),

    # image apis
    path('image/create', ImageCreateApiView.as_view(), name='image_create'),
    path('image/list/', ImageListApiView.as_view(), name='image_list'),
]
