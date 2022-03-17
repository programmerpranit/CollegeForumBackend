from django.shortcuts import render
from .models import Question

# Create your views here.

# make views here

# getlist of questions
def getListOfQuestions(request):
    
    # questionList = Question.objects.all()
    # return questionList
    pass


# add question 
def addQuestion(request):
    # verify jwt token
    # get all parameters from request
    # create a Question object 
    # save the object
    # return 200
    pass


def addAnswer(request):
    # verify jwt token 
    # GET Question id
    # create ans object
    # add forgein key as QuestionId
    # save Ans object
    pass

def getFullQuestion(request):
    # get Question by Question id
    # search for answers with same forgein key 
    # return object with question and answer 
    pass
