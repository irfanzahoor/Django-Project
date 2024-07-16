"""
URL configuration for nextash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nextash import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutus),
    path('',views.homePage),
    path('services/',views.services),
    path('404/',views.err),
    path('blog-details/',views.blog_details),
    path('blogs/',views.blogs),
    path('work/',views.work),
    path('faqs/',views.faqs),
    path('careers/',views.careers),
    path('team/',views.team),
    path('contact-us/',views.contactus),
    path('login/',views.login),
]
