from django.urls import include, path
from .views import UniversityCreateView

urlpatterns = [
    path('university/create/', UniversityCreateView.as_view(), 'university_create'),
]