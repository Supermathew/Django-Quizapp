from django.shortcuts import render
from django.shortcuts import render, redirect
from quiz_app.forms import Contactform,userres
from django.contrib import messages
from quiz_app.models import Contact,Quizcategory,Quizquestion,Usersubmitted,userattempt
from django.core.paginator import Paginator
from datetime import timedelta,datetime,timezone
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.

def index(request):
    allshops= Quizcategory.objects.all()
    return render(request,'quiz.html',{'allshops':allshops})

@login_required
def contact(request):
    if request.method == "POST":
       print("happyaman")
       usercontactform =Contactform(request.POST or None)
       if usercontactform.is_valid():
          instance=usercontactform.save(commit=False)
          instance.manage=request.user
          instance.save()
          print("happywala")
          messages.success(request,("Message Send Successfully!"))
       else:
          print("happywalaaaaa")
          for field, errors in usercontactform.errors.items():
              mess='{}-:{}'.format(field, ','.join(errors))
              
              messages.error(request,mess)

       return redirect('contact')
    else:
        contact_form=Contactform()
        return render(request,'contact.html',{'contact_form':contact_form})

def about(request):
    return render(request,'aboutus.html',{})

@login_required
def question(request,cat_id):
    cate = Quizcategory.objects.get(id=cat_id)
    cate.submit=True
    cate.save()


    question= Quizquestion.objects.filter(category=cate).order_by('id').first()
    now = datetime.now(timezone.utc)

    lastattempt=None
    futureattempt=None
    limit=24
    countattempt=userattempt.objects.filter(category=cate,user=request.user).count()
    if countattempt == 0:
       print("first attempt")
       userattempt.objects.create(user=request.user,category=cate)
       return render(request,'question.html',{'one_question':question,'cate':cate})
    else:
        latestattempt=userattempt.objects.filter(category=cate,user=request.user).order_by('-id').first()
        futureattempt=latestattempt.attempttime + timedelta(hours=limit)
        print(latestattempt.attempttime)
        print(timedelta(hours=limit))
        print(futureattempt,futureattempt)
        print(datetime.now(timezone.utc))
        print(timezone.now)
        if latestattempt and datetime.now() < futureattempt:
            remainingtime= futureattempt
            return render(request,'warning.html',{'latestattempt.attempttime':latestattempt.attempttime,'remainingtime':remainingtime})
        else:
            submitans=Usersubmitted.objects.filter(user=request.user,category=cat_id)
            submitans.delete()
            return render(request,'question.html',{'one_question':question,'cate':cate})



@login_required
def submit(request,cat_id,obj_id):
    print("mathew")
    if request.method =='POST':
        print("mathew123")
        que =Quizquestion.objects.get(pk=obj_id)
        cat=Quizcategory.objects.get(pk=cat_id)
        answer=request.POST.get('rightans', False)
        print(answer)
        if answer is False:
           print("else")
           messages.error(request,("please select the opttion"))
        #    return redirect('submit','/',cat_id,'/',obj_id)
           return redirect(request.META.get('HTTP_REFERER'))

           
        else:
           Usersubmitted.objects.create(user=request.user,question=que,rightans=answer,category=cat)
           cate = Quizcategory.objects.get(id=cat_id)
           

           




    cate = Quizcategory.objects.get(id=cat_id)
    question= Quizquestion.objects.filter(category=cate,id__gt=obj_id).exclude(id=obj_id).order_by('id').first()
    if question:
        return render(request,'question.html',{'one_question':question,'cate':cate})

    else:
        return redirect('index')



@login_required
def skiped(request,cat_id,obj_id):
    print("skipped kar deya")
    if request.method=='POST':
       print("skipped kar deya")
       que =Quizquestion.objects.get(pk=obj_id)
       cat=Quizcategory.objects.get(pk=cat_id)
       Usersubmitted.objects.create(user=request.user,question=que,rightans="Not submited",category=cat)

    cate = Quizcategory.objects.get(id=cat_id)
    cate.submit=True
    cate.save()
    question= Quizquestion.objects.filter(category=cate,id__gt=obj_id).exclude(id=obj_id).order_by('id').first()
    if question:
        return render(request,'question.html',{'one_question':question,'cate':cate})

    else:
        return redirect('index')

@login_required
def result(request,cat_id):
    res=Usersubmitted.objects.filter(user=request.user,category=cat_id)
    skip=Usersubmitted.objects.filter(user=request.user,rightans="Not submited",category=cat_id).count()
    attempt =Usersubmitted.objects.filter(user=request.user,category=cat_id).exclude(rightans="Not submited").count()
    rightans=0
    for row in res:
        if row.question.opt_ans == row.rightans:
            rightans+=1

    if attempt == 0:
        percentage=0
    else:
        percentage=(rightans*100)/attempt


    
    return render(request,'result.html',{'result':res,'skip':skip,'attempt':attempt,'rightans':rightans,'percentage':percentage})



        

    

    






