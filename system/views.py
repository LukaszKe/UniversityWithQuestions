from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import student_required

from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth import get_user_model
from .forms import StudentSignUpForm, CandidateSignUpForm, UniversityCreateForm, QuestionCreateForm

from .models import University, Question



User = get_user_model()

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def signup_start(request):
    return render(request, 'signup_start.html')

class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityCreateForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'university'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        university = form.save()
        return redirect('home')

class QuestionCreateView(FormView):
    template_name = 'registration/signup_form.html'
    form_class = QuestionCreateForm

    def form_valid(self, form):
        question = form.save(commit=False)
        question.owner = self.request.user
        question.save()
        text = form.cleaned_data['text']
        universities = form.cleaned_data['universities']

        university_list = University.objects.filter(pk__in=universities)
        for university in universities:
            question.universities.add(university)

        return redirect('questions')

@method_decorator([login_required, student_required], name='dispatch')
class QuestionListView(ListView):
    model = Question
    ordering = ('createdAt', )
    context_object_name = 'questions'
    template_name = 'system/questions/question_list.html'

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset