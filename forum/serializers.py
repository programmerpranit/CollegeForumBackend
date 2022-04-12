from rest_framework import serializers
from account.models import User
from forum.models import Answer, Question

class UserYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','year_of_study']


class QuestionSerializer(serializers.ModelSerializer):
    
    # user = Question.user.get_object
    # print(Question.user.uid)

    user = UserYearSerializer(Question.user, read_only=True)
    # print(owner.data)

    class Meta:
        model = Question
        fields = ['qid', 'question_text', 'timestamp', 'user']



class AnswersSerializer(serializers.ModelSerializer):
    user = UserYearSerializer(Answer.user, read_only=True)
    class Meta:
        model = Answer
        fields = ['aid', 'user', 'answer_text', 'likes', 'dislikes', 'timestamp']


class FullQuestionSerializer(serializers.ModelSerializer):
    # a = Answer.objects.filter(question = int(Question.qid)).all()
    
    user = UserYearSerializer(Answer.user, read_only=True)
    # answers = AnswersSerializer(data=a)
    class Meta:
        model = Question
        fields = ['qid', 'question_text', 'timestamp', 'user']



