from djongo import models

from account.models import User

# Create your models here.

class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=1000, default="")
    # image = models.ImageField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=1000, default="")
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    
