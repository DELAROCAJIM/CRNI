from django.db.models import fields
from django.forms import ModelForm
from .models import Chrono_all

class ChronoForm(ModelForm):
    class Meta:
        model= Chrono_all
        fields = ['customer_lastname', 'customer_firstname', 'customer_middleint', 
        'customer_address', 'customer_email', 'customer_contact', 'customer_product',
        'customer_color', 'customer_quantity', 'customer_price', 'customer_tprice', 'customer_paymethod']
        