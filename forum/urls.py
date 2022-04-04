from django.urls import path
from .views import AddAnswerView, AddQuestionView, FullQuestionView, GetListOfQuestionsView, SearchQuestionView

urlpatterns = [
    path('addquestion', AddQuestionView.as_view(), name="Add Question"),
    path('questions', GetListOfQuestionsView.as_view(), name="Add Question"),
    path('fullquestion', FullQuestionView.as_view(), name="Add Question"),
    path('addanswer', AddAnswerView.as_view(), name="Add Question"),
    path('search', SearchQuestionView.as_view(), name="Add Question"),
]