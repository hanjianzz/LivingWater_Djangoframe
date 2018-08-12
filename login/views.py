#coding:utf-8
from django.shortcuts import render
#from django.http import HttpRequest

def login(request):
    return render(request,'login.html')

def main(request):
    return render(request,'index1.html')