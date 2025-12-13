from django.urls import path
from . import views

urlpatterns = [
    path("",views.contactus,name="contactus"),
    path("forms/",views.forms,name="forms"),
    path("viewinfo/",views.viewinfo,name="viewinfo")
]
