from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('template_filter.urls')),
    path('aboutus/', views.aboutus,name="about"),
    path('contactus/', views.contactus,name="contact"),
    path('portfolio/', views.portfolio,name="portfolio"),

]
