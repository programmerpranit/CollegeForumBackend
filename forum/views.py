from CollegeForum.settings import SECRET_KEY
from forum.serializers import AnswersSerializer, FullQuestionSerializer, QuestionSerializer
from .models import Question, Answer
from account.models import User
from rest_framework.views import APIView
import datetime, jwt
from rest_framework.response import Response
from rest_framework import status
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

# Create your views here.

# make views here

def verifyUser(token):
    try:
        decodedToken = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = User.objects.filter(sub = decodedToken['sub']).first()
        return user
    except jwt.ExpiredSignatureError:
        return None


# getlist of questions
class GetListOfQuestionsView(APIView):
    def get(self, request):
        list = Question.objects.all()
        data = QuestionSerializer(list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

# to add question
class AddQuestionView(APIView):
    def post(self, request):
        user = verifyUser(request.data['jwttoken'])
        if user is None:
            return Response({'error': 'Authorization Failed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        question_text = request.data['question_text']
        # question_image = request.data['question_image']

        question = Question.objects.create(question_text=question_text, user = user)

        # if question_image is not None:
        #     question.image = question_image

        question.save()
        data = QuestionSerializer(question)
        return Response(data=data.data, status=status.HTTP_201_CREATED)

        
# to add answer
class AddAnswerView(APIView):
    def post(self, request):
        user = verifyUser(request.data['jwttoken'])
        if user is None:
            return Response({'error': 'Authorization Failed'}, status=status.HTTP_401_UNAUTHORIZED)
        answer_text = request.data['answer_text']
        qid = request.data['qid']
        question = Question.objects.filter(qid = qid).first()
        answer = Answer.objects.create(answer_text=answer_text, question = question, user = user)
        answer.save()
        data = AnswersSerializer(answer)
        return Response(data=data.data, status=status.HTTP_201_CREATED)


class FullQuestionView(APIView):
    def get(self, request):
        qid = self.request.query_params.get('qid')
        question = Question.objects.filter(qid = qid).first()
        answers = Answer.objects.filter(question = qid).all()
        serializedAnswers = AnswersSerializer(answers, many=True)
        serializedQuestion = FullQuestionSerializer(question)
        return Response({'question':serializedQuestion.data, 'answers': serializedAnswers.data}, status=status.HTTP_200_OK)


class SearchQuestionView(APIView):
    def get(self, request):
        q = self.request.query_params.get('q')

        query = SearchQuery(q)
        vector = SearchVector('question_text')

        questions = Question.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')

        questionsSerializer = QuestionSerializer(questions, many=True)

        return Response(questionsSerializer.data, status=status.HTTP_200_OK)
