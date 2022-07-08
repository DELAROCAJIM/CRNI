from django.shortcuts import render, redirect
from django.http import HttpResponse
from chronosys.forms import ChronoForm
from .models import *

def CustomerPage(request):
	return render(request, 'Chrono_model1_v2.html')

def Feedback(request):
	if request.method == 'POST':
		topic= request.POST['topic']
		message= request.POST['message']
		Chrono_feedback.objects.create(customer_topic = topic, customer_message = message)
	return render(request, 'Chrono_model4_v2.html')

def Summary(request):
	if request.method == 'POST':
		lastname= request.POST['lastname']
		firstname= request.POST['firstname']
		middlename= request.POST['middlename']
		address= request.POST['address']
		email= request.POST['email']
		contact= request.POST['contact']
		product= request.POST['product']
		color= request.POST['color']
		quantity= request.POST['quantity']
		price= request.POST['price']
		tprice= request.POST['tprice']
		pay= request.POST['pay']
		Chrono_all.objects.create(customer_lastname = lastname, customer_firstname = firstname,
		 customer_middleint = middlename, customer_address = address, customer_email = email , customer_contact = contact,
		 customer_product = product, customer_color = color, customer_quantity = quantity, customer_price = price, customer_tprice = tprice,
		customer_paymethod = pay)
	sChrono_all = Chrono_all.objects.all()
	sChrono_feedback = Chrono_feedback.objects.all()
	return render(request, 'Chrono_model2_v2.html', {'Chrono_all':sChrono_all,'Chrono_feedback':sChrono_feedback})
def edit(request, id):
	custom = Chrono_all.objects.get(id=id)
	form = ChronoForm(instance=custom)
	if request.method == 'POST':
		form = ChronoForm(request.POST, instance = custom)
		if form.is_valid():
			form.save()
			return redirect('/Summary')

	return render(request, 'edit.html', {'form':form})
		
def delete(request, id):
    Chrono = Chrono_all.objects.get(id=id)
    for x in Chrono_all.objects.only('id'):
        if Chrono == x:
            x = Chrono_all.objects.get(id=id).delete()
            break
    return redirect('/Summary')

def Delete1(request, id):
    Chrono = Chrono_feedback.objects.get(id=id)
    for x in Chrono_feedback.objects.only('id'):
        if Chrono == x:
            x = Chrono_feedback.objects.get(id=id).delete()
            break
    return redirect('/Summary')