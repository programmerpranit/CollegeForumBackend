from django.db import models
from account.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=1000, default="")
    # image = models.ImageField(upload_to=nameFile , blank=True, null=True)
    image = CloudinaryField('image', null=True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     indexes = [
    #         'fields' : ['question_text']
    #     ]

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=1000, default="")
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0) 
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.answer_text
