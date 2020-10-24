from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserResult(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    operator = models.CharField(max_length=3)
    result = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)    

'''
python manage.py makemigrations -> starts the migrations
python manage.py sqlmigrate paid 0001 -> convert the model into sql queries
python manage.py migrate -> will run that sql query in the database (settings.py file)
'''