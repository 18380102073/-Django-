from django.contrib import admin
from django.urls import path,include
from killer import sing_out
urlpatterns = [
    path('test',sing_out.test),
    path('userLogin',sing_out.signin),
    path('userOut',sing_out.signout),
    path('test1',sing_out.test1),
    path('loadlabeldata',sing_out.loadLabelData),
]