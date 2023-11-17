from django.shortcuts import render, redirect
from .models import Codesnippet
from django.http import HttpResponse, JsonResponse
import secrets

def CreatePost(request):
    if request.method == 'POST':
        code = request.POST['code']
        category=request.POST['category']
        Codesnippet.objects.create(code=code, category=category)
        url=Codesnippet.objects.latest('id')
        newUrl = '/view/'+str(url.id)
        return redirect(newUrl)
        return render(request, "post.html", {'status':'success' })
    return render(request, "post.html")

def viewCode(request, pk):
    code = Codesnippet.objects.get(id=pk)
    return render(request, "code.html", {'code':code})

def listCodes(request):
    codes = Codesnippet.objects.all()
    return render(request, "viewposts.html", {'data':codes})