from django.urls import path 
from .views import CreateAccountView , DetailAccountView ,Register , Login


urlpatterns = [
    path('register/', Register.as_view(), name='register_api'),
    path('login/', Login.as_view(), name='login_api'),
	path('account/', CreateAccountView.as_view(), name='create_account'),
	path('account/update/<pk>', DetailAccountView.as_view(), name='account_detail'),

]