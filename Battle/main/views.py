from django.shortcuts import render
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseNotFound, Http404




def index(request):
    return render(request, "main/site.html")


def prizes(request):
    return render(request, "prizes/prizes2.html")


def registration(request):
    return render(request, "reg/registration.html")


def new_game(request):
    return render(request, "main/new_game.html")


def login(request):
    return render(request, "main/login.html")


#class RegisterUser(DataMixin, CreateView):


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Stranitsa ne naydena</h1>')

