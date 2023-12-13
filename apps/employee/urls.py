from django.urls import path, include
from apps.employee.api_endpoints.employee import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'activity', views.ActivityView)

urlpatterns = [
    path('employee/list', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/create', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>', views.EmployeeDestroyView.as_view(), name='employee_delete'),
    
    # path('activity', views.ActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    # path('workactivity', views.WorkActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('socialmedia', views.SocialMediaView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]