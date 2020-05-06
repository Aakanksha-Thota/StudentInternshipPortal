from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup1
from .models import Intern
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm

def apphome(request):
    return render(request,'web_app/apphome.html')


@login_required
def interns(request):
    context=Intern.objects.all()
    return render(request,'web_app/interns.html',{'context':context})

@login_required
def status(request):
    user=request.user.get_full_name()
    context=Signup1.objects.all().filter(full_name=user)
    return render(request,'web_app/status.html',{'context':context})

@login_required
def appl(request):  
    if request.method == "POST":
        full_name = request.POST["full_name"] 
        if full_name==request.user.get_full_name(): 
            gender = request.POST["gender"]
            phone_no = request.POST["phone_no"]
            email_id= request.POST["email"] 
            internship_id= request.POST["internship_id"]
            resume_file=request.FILES["resume_file"]    
            post = Signup1(full_name=full_name,gender=gender,phone_no=phone_no,email=email_id,internship_id=internship_id,resume_file=resume_file)
            form =ApplicationForm(request.POST) 
            try:
                post.validate_unique()
            except:
                messages.warning(request, 'Already applied for this internship')
                return render(request,'web_app/apphome.html')

            try:
                post.full_clean()
            except:
                messages.warning(request, 'Phone number not valid')
                form =ApplicationForm() 
                return render(request,'web_app/application.html',{'form':form})  
                  
            post.save()
            messages.success(request, 'Applied for the internship succesfully')
            return render(request,'web_app/apphome.html') 
             
        else:
            messages.warning(request, 'Full name does not match')
            form =ApplicationForm() 
            return render(request,'web_app/application.html',{'form':form})
    else:  
        form =ApplicationForm()  
        return render(request,'web_app/application.html',{'form':form})  


