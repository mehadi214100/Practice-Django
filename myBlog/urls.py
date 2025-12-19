from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('template_filter.urls')),
    path('contactus/', include('djangoForms.urls')),
    path('hackathon/', include('hackathon.urls')),
    path('aboutus/', views.aboutus,name="about"),
    path('portfolio/', views.portfolio,name="portfolio"),

]
