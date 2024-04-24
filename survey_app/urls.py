from django.urls import path
from . import views

urlpatterns = [
    path('surveys/', views.SurveyListCreateView.as_view(), name='survey-list-create'),
    path('surveys/<int:pk>/', views.SurveyDetailView.as_view(), name='survey-detail'),
    path('questions/', views.QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('responses/', views.ResponseListCreateView.as_view(), name='response-list-create'),
    path('responses/<int:pk>/', views.ResponseDetailView.as_view(), name='response-detail'),
    path('answers/', views.AnswerListCreateView.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', views.AnswerDetailView.as_view(), name='answer-detail'),
]
