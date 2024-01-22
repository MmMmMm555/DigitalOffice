from django.urls import path

from apps.employee.api_endpoints.employee import views
from apps.employee.api_endpoints.department.views import DepartmentAPIView, PositionAPIView
from apps.employee.api_endpoints.universities.views import GraduationAPIView


urlpatterns = [
    path('employee/list', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/create', views.EmployeeCreateView.as_view(),
         name='employee_create'),
    path('employee/update/<int:pk>',
         views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>',
         views.EmployeeDetailView.as_view(), name='employee_detail'),

    # path('activity', views.ActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    # path('workactivity', views.WorkActivityView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('socialmedia', views.SocialMediaView.as_view(
        {'get': 'list', 'post': 'create', })),
    path('socialmedia/<int:pk>',
         views.SocialMediaView.as_view({'put': 'update', 'delete': 'destroy'})),

    # departments api
    path('department', DepartmentAPIView.as_view(
        {'get': 'list'}), name='department_list'),
    path('position', PositionAPIView.as_view(
        {'get': 'list'}), name='position_list'),

    # universities api
    path('university', GraduationAPIView.as_view(), name='university_list'),
    
    # excel
    path('excel', views.EmployeeExcelData.as_view(), name='employee_excel'),
]
