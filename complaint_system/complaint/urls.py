from django.urls import path 
from complaint.api.views import ListCreatComplaintView , SingleComplaintView

urlpatterns = [
    path('complaint/', ListCreatComplaintView.as_view(), name='complaints'),
    path('complaint/<int:id>/',SingleComplaintView.as_view(), name='comlaint')
]
