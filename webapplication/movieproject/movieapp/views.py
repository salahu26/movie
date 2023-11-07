from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movies
from . forms import movieforms
# Create your views here.
def index(result):
    abc=movies.objects.all()
    content={'movie_list':abc}
    return render(result,'index.html',content)
def detail(value,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(value,'detail.html',{'abc':movie})
 #   return HttpResponse("this the movie number %s " % movie_id)

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get("name",)
        des = request.POST.get("des",)
        year = request.POST.get("year",)
        img = request.FILES["img"]
        movie=movies(name=name,des=des,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    form=movieforms(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'form':form, 'abc':movie})

def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
