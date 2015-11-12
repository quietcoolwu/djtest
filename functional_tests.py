from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrive_it_later(self):
        #check out the home page
        self.browser.get('http://localhost:8000')
        
        #Notice the 'To-Do' word
        self.assertIn('To-Do', self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #invite her to input
        input = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
      
        )
        #input by user
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(keys.ENTER)
        
        table= self.browser.find_element_by_id('id_last_table')
        rows= self.browser.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text=='1:Buy peacock feathers' for rows in rows)
        )
        
        self.fail('Finish the Test!')
    

if __name__ == '__main__':
    unittest.main(warnings='ignore')