from django.shortcuts import render

def deneme(request):
    return render(request, 'users/deneme.html' )