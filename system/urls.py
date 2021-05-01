from django.urls import include, path
from .views import UniversityCreateView, QuestionCreateView, QuestionListView

urlpatterns = [
    path('university/create/', UniversityCreateView.as_view(), 'university_create'),
    path('question/create/', QuestionCreateView.as_view(), 'question_create'),
    path('questions/', QuestionListView.as_view(), name='questions'),
]