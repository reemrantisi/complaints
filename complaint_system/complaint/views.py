import logging
from django.core.mail import EmailMessage
from complaint_system.settings import EMAIL_HOST_USER
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ComplaintForm 
from .models import Complaint

# Create your views here.

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def home_view(request):
    user = request.user
    complaints = Complaint.objects.all()
    if not user.is_authenticated:
        return redirect("login")
    if request.method == 'POST' :
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid() :
            complaint = form.save(commit= False)
            complaint.image = request.FILES['image']
            file_type = complaint.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return HttpResponse('invalid file type')
            complaint.save()
            subject = complaint.title
            message = complaint.description 
            logging.warning(message)
            email = EmailMessage(subject , message , EMAIL_HOST_USER , [EMAIL_HOST_USER],)
            uploaded_file = request.FILES['image']
            email.attach(uploaded_file.name,uploaded_file.read(), uploaded_file.content_type)
            email.send()
            return render(request,'complaint/home.html')
    
    context = {
        "form" : ComplaintForm,
        "complaints" : complaints
    }
    
    return render(request,'complaint/home.html', context)
