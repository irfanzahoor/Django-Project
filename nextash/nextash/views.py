from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render

def aboutus(request):
  return render(request ,"about-us.html")
def services(request):
  return render(request, 'services.html')
def homePage(request):
  return render(request,"index.html")
def err(request):
  return render(request,"404.html") 
def blog_details(request):
  return render(request,"blog-details.html") 
def blogs(request):
  return render(request,"blogs.html") 
def work(request):
  return render(request,"work.html") 
def team(request):
  return render(request,"team.html") 
def contactus(request):
  return render(request,"contact-us.html") 
def careers(request):
  return render(request,"careers.html") 
def faqs(request):
  return render(request,"faqs.html") 
def login(request):
  data = {}
  try:
      if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
      data = {
        'name' : name,
        'email' : email
      }
      return HttpResponseRedirect("index.html/")
  except:
    pass
  return render(request,"login.html",data) 
 