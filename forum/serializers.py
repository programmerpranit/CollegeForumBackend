from dataclasses import fields
from rest_framework import serializers
from account.models import User
from forum.models import Answer, Question

class UserYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid','name','year_of_study']


class QuestionSerializer(serializers.ModelSerializer):
    
    user = Question.user.get_object

    owner = UserYearSerializer(user, read_only=True)


    class Meta:
        model = Question
        fields = ['qid', 'question_text', 'timestamp', 'owner']

class AnswersSerializer(serializers.ModelSerializer):
    owner = UserYearSerializer(Answer.user, read_only=True)
    class Meta:
        model = Answer
        fields = ['aid', 'owner', 'answer_text', 'likes', 'dislikes', 'timestamp']


class FullQuestionSerializer(serializers.ModelSerializer):
    # a = Answer.objects.filter(question = int(Question.qid)).all()
    
    owner = UserYearSerializer(Answer.user, read_only=True)
    # answers = AnswersSerializer(data=a)
    class Meta:
        model = Question
        fields = ['qid', 'question_text', 'timestamp', 'owner']



