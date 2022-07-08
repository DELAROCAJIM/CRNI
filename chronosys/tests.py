from urllib import response
from django.test import TestCase
from chronosys.views import MainPage
from .models import ChronoBreak_form
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'inqname' :'Jim Ryan Dela Roca',
	 		'inqemail': 'jimryan.delaroca@gmail.com',
	 		'inqinquiry': 'General Inquiry',
	 		'inqcontact': '0919-644-4703',
	 		'inqmessage': 'I have a message'})
		self.assertEqual(ChronoBreak_form.objects.count(),1)
		inputData = ChronoBreak_form.objects.first()
		self.assertEqual(inputData.chrono_name, 'Jim Ryan Dela Roca')
		self.assertEqual(inputData.chrono_email, 'jimryan.delaroca@gmail.com')
		self.assertEqual(inputData.chrono_inquiry, 'General Inquiry')
		self.assertEqual(inputData.chrono_contact, '0919-644-4703')
		self.assertEqual(inputData.chrono_message, 'I have a message')

	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(ChronoBreak_form.objects.count(), 0)

	def test_POST_redirect(self):
		response = self.client.post('/', {'inqname' :'Jim Ryan Dela Roca',
	 		'inqemail': 'jimryan.delaroca@gmail.com',
	 		'inqinquiry': 'General Inquiry',
	 		'inqcontact': '0919-644-4703',
	 		'inqmessage': 'I have a message'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


	class ORMTEST(TestCase):
		def test_saving_retrive(self):
			ChronoBreak_form_1 = ChronoBreak_form()
			ChronoBreak_form_1.chrono_name = 'Jim Ryan Dela Roca'
			ChronoBreak_form_1.chrono_email = 'jimryan.delaroca@gmail.com'
			ChronoBreak_form_1.chrono_inquiry = 'General Inquiry'
			ChronoBreak_form_1.chrono_contact = '0919-644-4703'
			ChronoBreak_form_1.chrono_message = 'I have a message'
			ChronoBreak_form_1.save()

			ChronoBreak_form_2 = ChronoBreak_form()
			ChronoBreak_form_2.chrono_name = 'FlashyFlash'
			ChronoBreak_form_2.chrono_email = 'flashyflash@gmail.com'
			ChronoBreak_form_2.chrono_inquiry = 'Subscription'
			ChronoBreak_form_2.chrono_contact = '0916-655-4813'
			ChronoBreak_form_2.chrono_message = 'I have a subscription'
			ChronoBreak_form_2.save()

			ChronoBreak_Contact = ChronoBreak_form.objects.all()
			self.assertEqual(ChronoBreak_Contact.count(), 2)

			chronoinput1 = ChronoBreak_Contact[0]
			chronoinput2 = ChronoBreak_Contact[1]

			self.assertEqual(chronoinput1.chrono_name, 'Jim Ryan Dela Roca')
			self.assertEqual(chronoinput1.chrono_email, 'jimryan.delaroca@gmail.com')
			self.assertEqual(chronoinput1.chrono_inquiry, 'General Inquiry')
			self.assertEqual(chronoinput1.chrono_contact, '0919-644-4703')
			self.assertEqual(chronoinput1.chrono_message, 'I have a message')

			self.assertEqual(chronoinput2.chrono_name, 'FlashyFlash')
			self.assertEqual(chronoinput2.chrono_email, 'flashyflash@gmail.com')
			self.assertEqual(chronoinput2.chrono_inquiry, 'Subscription')
			self.assertEqual(chronoinput2.chrono_contact, '0916-655-4813')
			self.assertEqual(chronoinput2.chrono_message, 'I have a subscription')

	def test_template_display_list(self):
		ChronoBreak_form.objects.create(chrono_name = "Jim Ryan Dela Roca", chrono_email = 'jimryan.delaroca@gmail.com', chrono_inquiry = 'General Inquiry', chrono_contact = '0919-644-4703', chrono_message = 'I have a message')
		ChronoBreak_form.objects.create(chrono_name = "FlashyFlash", chrono_email = 'flashyflash@gmail.com', chrono_inquiry = 'Subscription', chrono_contact = '0916-655-4813', chrono_message = 'I have a subscription')
		response = self.client.get('/')
		self.assertIn('1: Jim Ryan Dela Roca, jimryan.delaroca@gmail.com, General Inquiry, 0919-644-4703, I have a message', response.content.decode())
		self.assertIn('2: FlashyFlash, flashyflash@gmail.com, Subscription, 0916-655-4813, I have a subscription', response.content.decode())