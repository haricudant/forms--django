from django.shortcuts import render
from django.http import HttpResponse
from myapp import  forms

def index(requests):
    voot={'ll':"I AM FROM THE HOME PAGE and go to '/forms' to fill the form" }
    return render(requests,'index.html',context=voot)

def form_name_view(requests):
    form = forms.FormNames()

    if requests.method=='POST':
         form= forms.FormNames(requests.POST)

         if form.is_valid():
            print("Validation success")
            print("name:" +form.cleaned_data['Name'])
            print("email:" +form.cleaned_data['email'])
            print("Text:" +form.cleaned_data['text'])
    return render(requests,'forms_name.html',{'form':form})

# Create your views here.
