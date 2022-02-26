# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
#from django.views.decorators import csrf


def index(request):
    context = {}
    if(request.GET):
        entity = request.GET['user_text']
        context = {'user_text':entity}
        return render(request, 'entity.html', context)
    return render(request, 'index.html', context)
