from django.urls import path
from addapp import views

app_name='add'
urlpatterns =[
    # path('add/',views.add,name='add'),
    path('addlogic/',views.addlogic,name='addlogic'),
    path('emplist/',views.emplist,name='emplist'),
    path('update/',views.update,name='update'),
    path('updatelogic/',views.updatelogic,name='updatelogic'),
    path('delete/',views.delete,name='delete'),
    path('update3/',views.update3,name='update3'),

]