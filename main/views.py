from django.shortcuts import render,redirect
from . import models


def index(request):
    main_page = models.Main_page.objects.all()
    service = models.Service.objects.all()
    blog = models.Blog.objects.all()
    contact = models.Contact.objects.all()

    context = {
        'main_page':main_page,
        'service':service,
        'blog':blog,
        'contact':contact,
    }
    return render(request, 'index.html', context)


def servises(request):
    if request.method == 'POST':
        models.Service.objects.create(
            title = request.POST['title'],
            body = request.POST['body'],
            icon = request.POST['icon'],

        )
    return render(request, 'servises.html')



def blogs(request):
    if request.method == 'POST':
        models.Blog.objects.create(
            title = request.POST['title'],
            body = request.POST['body'],
            icon = request.POST['icon'],

        )
    return render(request, 'blog.html')



def contacts(request):
    if request.method == 'POST':
        models.Contact.objects.create(
            title = request.POST['title'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            body = request.POST['body'],

        )
        return redirect('index')
    return render(request, 'contact.html')