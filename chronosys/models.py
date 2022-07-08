from django.db import models

class Chrono_all(models.Model):
	customer_lastname = models.CharField(blank = True, max_length= 100)
	customer_firstname = models.CharField(blank = True, max_length= 100)
	customer_middleint = models.CharField(blank = True, max_length= 50)
	customer_address = models.CharField(blank = True, max_length= 120)
	customer_email = models.CharField(blank = True, max_length= 100)
	customer_contact = models.CharField(blank = True, max_length= 100)
	customer_product = models.CharField(blank = True, max_length= 100)
	customer_color = models.CharField(blank = True, max_length= 100)
	customer_quantity = models.CharField(blank = True, max_length= 100)
	customer_price = models.CharField(blank = True, max_length= 100)
	customer_tprice = models.CharField(blank = True, max_length= 100)
	customer_paymethod = models.CharField(blank = True, max_length= 100)
class Chrono_feedback(models.Model):
	customer_topic = models.CharField(blank = True, max_length= 100)
	customer_message = models.CharField(blank = True, max_length= 100)

