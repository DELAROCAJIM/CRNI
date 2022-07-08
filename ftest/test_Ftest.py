from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)

		self.assertIn('Chrono Intelligence',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('CHRONO INTELLIGENCE', headerText)

		InquirerName = self.browser.find_element_by_id('netizenName')
		self.assertEqual(InquirerName.get_attribute('placeholder'),'Type Your Name.')
		InquirerName.send_keys('Jim Ryan Dela Roca')
		time.sleep(1)

		InquirerEmail = self.browser.find_element_by_id('netizenEmail')
		self.assertEqual(InquirerEmail.get_attribute('placeholder'),'Type Your E-mail.')
		InquirerEmail.send_keys('jimryan.delaroca@gmail.com')
		time.sleep(1)

		InquirerInquiry = self.browser.find_element_by_id('netizenInquiry')
		self.assertEqual(InquirerInquiry.get_attribute('placeholder'),'State Your Inquiry.')
		selectInquirerInquiry = Select(InquirerInquiry)
		selectInquirerInquiry.select_by_visible_text('General Inquiry')
		time.sleep(1)

		InquirerContact = self.browser.find_element_by_id('netizenContact')
		self.assertEqual(InquirerContact.get_attribute('placeholder'),'Type Your Contact Number.')
		InquirerContact.send_keys('0916-470-3806')
		time.sleep(1)

		InquirerMessage = self.browser.find_element_by_id('netizenMessage')
		self.assertEqual(InquirerMessage.get_attribute('placeholder'),'Type Your Message Here.')
		InquirerMessage.send_keys('I have a message')
		time.sleep(1)
      		
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)

	def test_start_list_and_retrieve_2(self):
		self.browser.get(self.live_server_url)

		self.assertIn('Chrono Intelligence',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('CHRONO INTELLIGENCE', headerText)

		InquirerName = self.browser.find_element_by_id('netizenName')
		self.assertEqual(InquirerName.get_attribute('placeholder'),'Type Your Name.')
		InquirerName.send_keys('FlashyFlash')
		time.sleep(1)

		InquirerEmail = self.browser.find_element_by_id('netizenEmail')
		self.assertEqual(InquirerEmail.get_attribute('placeholder'),'Type Your E-mail.')
		InquirerEmail.send_keys('flashyflash@gmail.com')
		time.sleep(1)

		InquirerInquiry = self.browser.find_element_by_id('netizenInquiry')
		self.assertEqual(InquirerInquiry.get_attribute('placeholder'),'State Your Inquiry.')
		selectInquirerInquiry = Select(InquirerInquiry)
		selectInquirerInquiry.select_by_visible_text('Subscription')
		time.sleep(1)

		InquirerContact = self.browser.find_element_by_id('netizenContact')
		self.assertEqual(InquirerContact.get_attribute('placeholder'),'Type Your Contact Number.')
		InquirerContact.send_keys('0916-655-4813')
		time.sleep(1)

		InquirerMessage = self.browser.find_element_by_id('netizenMessage')
		self.assertEqual(InquirerMessage.get_attribute('placeholder'),'Type Your Message Here.')
		InquirerMessage.send_keys('I have a subscription')
		time.sleep(1)
      		
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)

#---2nd

		InquirerName = self.browser.find_element_by_id('netizenName')
		self.assertEqual(InquirerName.get_attribute('placeholder'),'Type Your Name.')
		InquirerName.send_keys('Jim Ryan Dela Roca')
		time.sleep(1)

		InquirerEmail = self.browser.find_element_by_id('netizenEmail')
		self.assertEqual(InquirerEmail.get_attribute('placeholder'),'Type Your E-mail.')
		InquirerEmail.send_keys('jimryan.delaroca@gmail.com')
		time.sleep(1)

		InquirerInquiry = self.browser.find_element_by_id('netizenInquiry')
		self.assertEqual(InquirerInquiry.get_attribute('placeholder'),'State Your Inquiry.')
		selectInquirerInquiry = Select(InquirerInquiry)
		selectInquirerInquiry.select_by_visible_text('General Inquiry')
		time.sleep(1)

		InquirerContact = self.browser.find_element_by_id('netizenContact')
		self.assertEqual(InquirerContact.get_attribute('placeholder'),'Type Your Contact Number.')
		InquirerContact.send_keys('0916-470-3806')
		time.sleep(1)

		InquirerMessage = self.browser.find_element_by_id('netizenMessage')
		self.assertEqual(InquirerMessage.get_attribute('placeholder'),'Type Your Message Here.')
		InquirerMessage.send_keys('I have a message')
		time.sleep(1)
      		
		btnSubmit = self.browser.find_element_by_id('btnSubmit')
		btnSubmit.click()
		time.sleep(1)

		table = self.browser.find_element_by_id('netizenDetails')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: FlashyFlash, flashyflash@gmail.com, Subscription, 0916-655-4813, I have a subscription', [row.text for row in row_data])
		self.assertIn('2: Jim Ryan Dela Roca, jimryan.delaroca@gmail.com, General Inquiry, 0916-470-3806, I have a message', [row.text for row in row_data])
		
#if __name__ == '__main__' :
#	unittest.main(warnings='ignore')