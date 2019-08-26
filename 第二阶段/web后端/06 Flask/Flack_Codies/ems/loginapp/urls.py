from django.urls import path
from loginapp import views

app_name='loginapp'
urlpatterns = [
    # path('regist/',views.regist,name='regist'),
    path('login/',views.login,name='login'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('captcha/',views.captcha,name='captcha'),
    path('checkname/',views.checkname,name='checkname'),
    path('checkpwd/',views.checkpwd,name='checkpwd'),
    path('changecode/',views.changecode,name='changecode'),

]