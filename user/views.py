from django.shortcuts import render,redirect

from user.models import Blog
from .forms import Inscription
# Create your views here.
def utilisateur(request):
    blogs=Blog.objects.all()
    return render (request,'acceuil.html',{'blogs':blogs})


def inscription_views(request):
    if request.method=='POST':
        form=Inscription(request.POST)
        if form.is_valid():
            form=Inscription()
            return render( request,'valide.html',{'form':form})


    else:
        form=Inscription()
        return render(request,'inscription.html',{'form':form})

