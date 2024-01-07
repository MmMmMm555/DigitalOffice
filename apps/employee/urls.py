from django.urls import path, include

from apps.employee.api_endpoints.employee import views
from apps.employee.api_endpoints.department.views import DepartmentAPIView


urlpatterns = [
    path('employee/list', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/create', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>', views.EmployeeDestroyView.as_view(), name='employee_delete'),

     # path('activity', views.ActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
     # path('workactivity', views.WorkActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('socialmedia', views.SocialMediaView.as_view({'get': 'list', 'post': 'create',})),
    path('socialmedia/<int:pk>', views.SocialMediaView.as_view({'put': 'update', 'delete': 'destroy'})),
    
    path('department', DepartmentAPIView.as_view({'get': 'list'}), name='department_list'),
    path('department/<int:pk>', DepartmentAPIView.as_view({'delete': 'destroy'}), name='department_list'),
]