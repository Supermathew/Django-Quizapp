from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Quizcategory(models.Model):
    title=models.TextField(max_length=200)
    details =models.TextField(max_length=200)
    image=models.ImageField(upload_to='cat_img/')
    submit=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='category'

    


    def __str__(self):
        return self.title


class Quizquestion(models.Model):
    question=models.TextField(max_length=200)
    opt_1=models.TextField(max_length=200)
    opt_2=models.TextField(max_length=200)
    opt_3=models.TextField(max_length=200)
    opt_4=models.TextField(max_length=200)
    opt_ans=models.TextField(max_length=200)
    time_limit=models.IntegerField()
    category=models.ForeignKey(Quizcategory,on_delete=models.CASCADE)


    class Meta:
         verbose_name_plural='question'

    def __str__(self):
       return self.question

class Contact(models.Model):
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=300)
    email=models.EmailField(max_length=254)
    message= models.CharField(max_length=350)

    def __str__(self):
        return self.message


class Usersubmitted(models.Model):
     question=models.ForeignKey(Quizquestion,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     rightans=models.TextField(max_length=200,null=True)
     category=models.ForeignKey(Quizcategory,on_delete=models.CASCADE)

     def __str__(self):
        return self.rightans


     class Meta:
        verbose_name_plural='Usersubmitedresponce'

class userattempt(models.Model):
     category=models.ForeignKey(Quizcategory,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     attempttime=models.DateTimeField(auto_now_add=True)

     class Meta:
        verbose_name_plural='Userattempt'

     
  

   


    
