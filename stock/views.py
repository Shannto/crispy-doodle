from stock.order import ProductForm,InvoiceForm,ProductForm2
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import History, Product
from django.db import transaction
from django.db import IntegrityError,Error
from django.db.models import F
from django.forms import inlineformset_factory


# Create your views here.


def createProduct(request):
    obj = Product()
    form = ProductForm2()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ProductForm2(request.POST)
        if form.is_valid():
            form.save()
            

    context = {'form':form}
    return render(request, 'createProduct.html', context)

def stockIn(request):
    item = Product.objects
    form=ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            feet1 = form.cleaned_data['feet']
            mm1 = form.cleaned_data['mm']
            types1 = form.cleaned_data['types']
            piece1 = form.cleaned_data['pieces']

            Product.objects.select_for_update().filter(feet=feet1,mm=mm1,types=types1).update(pieces = F('pieces')+piece1)


            obj = History() #gets new object
            obj.date = form.cleaned_data['date']
            obj.pieces = form.cleaned_data['pieces']
            obj.feet = form.cleaned_data['feet']
            obj.mm = form.cleaned_data['mm']
            obj.types = form.cleaned_data['types']
            obj.name = 'মাল আসিয়াছে'
            #finally save the object in db
            obj.save()
            



    return render(request,'stockIn.html',{'form':form})


def showHistory(request):
    sales=History.objects.all()

    return render(request,'history.html',{'sales':sales})

def stock(request):
    i=Product.objects.order_by('mm')
    return render(request,'stock.html',{'i':i})

def sales(request):
    item = Product.objects
    form=ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            feet1 = form.cleaned_data['feet']
            mm1 = form.cleaned_data['mm']
            types1 = form.cleaned_data['types']
            piece1 = form.cleaned_data['pieces']

            Product.objects.select_for_update().filter(feet=feet1,mm=mm1,types=types1).update(pieces = F('pieces')-piece1)


            obj = History() #gets new object
            obj.date = form.cleaned_data['date']
            obj.pieces = form.cleaned_data['pieces']
            obj.feet = form.cleaned_data['feet']
            obj.mm = form.cleaned_data['mm']
            obj.types = form.cleaned_data['types']
            obj.name = 'বিক্রয়'
            #finally save the object in db
            obj.save()
            



    return render(request,'sales.html',{'form':form})

def showProducts(request):
    prod=Product.objects.order_by('mm')

    return render(request,'products.html',{'products':prod})


def invoice(request):
    

    return render(request,'invoice.html',{})

def index(request):
     
   MyLoginForm = InvoiceForm()
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = InvoiceForm(request.POST)
      
      if MyLoginForm.is_valid():
         qty = MyLoginForm.cleaned_data['qty']
         fts = MyLoginForm.cleaned_data['fts']
         bun = MyLoginForm.cleaned_data['bun']
		
   return render(request, 'index.html', {"MyLoginForm" : MyLoginForm})

def newview(request,pk):
    
    
    s= Product.objects.filter(mm=pk)

    return render(request, 'newview.html', {'s':s,'pk':pk})