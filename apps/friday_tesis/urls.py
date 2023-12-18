from django.urls import path
from apps.friday_tesis.api_endpoints.tesis.views import (FridayTesisCreateView, 
                                                         FridayTesisListView,
                                                         FridayTesisUpdateView,
                                                         FridayTesisDeleteView)
from apps.friday_tesis.api_endpoints.seen_api.views import (FridayTesisImamReadView, 
                                                            FridayTesisImamReadListView)
from apps.friday_tesis.api_endpoints.results_api.views import FridayTesisImamResultView, FridayTesisImamResultListView

urlpatterns = [
     # tesis apis
     path('create/', FridayTesisCreateView.as_view(), name='tesis_create'),
     path('update/<int:pk>/', FridayTesisUpdateView.as_view(), name='tesis_update'),
     path('delete/<int:pk>/', FridayTesisDeleteView.as_view(), name='tesis_delete'),
     path('list/', FridayTesisListView.as_view(), name='tesis_list'),

     # seen apis
     path('seen/create', FridayTesisImamReadView.as_view(), name='tesis_seen'),
     path('seen/list', FridayTesisImamReadListView.as_view(), name='tesis_seen_list'),
     
     # result apis
     path('result/create', FridayTesisImamResultView.as_view(), name='result_create'),
     path('result/list', FridayTesisImamResultListView.as_view(), name='result_list'),

]