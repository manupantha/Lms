from django.shortcuts import render
from library.models import Member, Magazine
from django.http import HttpResponse
# Create your views here.


def index_view(request):
    context = {

    }
    return render(request, "index.html", context)

