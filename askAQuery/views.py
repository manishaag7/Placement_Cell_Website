from django.shortcuts import render
from django.http import HttpResponse
from .models import Query, CommentOnQuery
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    queries = Query.objects.all()
    context = {
        'title' : 'Ask Away...!',
        'queries' : queries,
    }
    return render(request,'askAQuery/home.html',context)