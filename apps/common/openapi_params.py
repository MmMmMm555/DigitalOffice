from drf_yasg import openapi
from apps.employee.models import AcademicDegree
from apps.common.regions import Regions

region = openapi.Parameter(name="region", in_=openapi.IN_FORM, type='array', items=AcademicDegree.choices, description="regions_choice")
district = openapi.Parameter(name="district", in_=openapi.IN_QUERY, type='array', items=AcademicDegree.choices, description="district_choice")
start_date = openapi.Parameter(name="start_date", in_=openapi.IN_QUERY, type="date", description="start_date")
finish_date = openapi.Parameter(name="finish_date", in_=openapi.IN_QUERY, type="date", description="finish_date")
