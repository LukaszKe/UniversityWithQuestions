from django.urls import include, path
from .views import UniversityCreateView, QuestionCreateView, QuestionListView

urlpatterns = [
    path('university/create/', UniversityCreateView.as_view(), name='university_create'),
    path('question/create/', QuestionCreateView.as_view(), name='question_create'),
    path('questions/', QuestionListView.as_view(), name='questions'),
]