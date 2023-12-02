from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        # Удовлетворенный, Коля уходит спать
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Коля услышал о новом крутом приложении для отслеживания задач
        # Он переходит на главную страницу приложения
        self.browser.get(self.live_server_url)

        # Он видит, что в названии страницы и хэдере упомянуты To-do листы
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element('tag name', 'h1').text
        self.assertIn('To-Do', header_text)

        # Коле предлагают с ходу написать задачу
        inputbox = self.browser.find_element('id', 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Он вводит "Купить новую кастрюлю на улицу" в текст-бокс
        # (Коля очень бедный и пьет только дождевую воду из кастрюли)
        inputbox.send_keys('Купить новую кастрюлю на улицу')

        # Он нажимает Enter, страница обновляется и теперь в 
        # To-do листе есть его запись - 1. "Купить новую кастрюлю на улицу"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1. Купить новую кастрюлю на улицу')

        # Текст бокс с приглашением написать еще одну задачу не пропал
        # Коля вводит "Молиться Перуну чтобы пошел дождь" (Коля практикует язычество)
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('Молиться Перуну чтобы пошел дождь')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Страница снова обновляется и теперь в списке есть две записи
        self.check_for_row_in_list_table('1. Купить новую кастрюлю на улицу')
        self.check_for_row_in_list_table('2. Молиться Перуну чтобы пошел дождь')
        
        # Коля гадает, запомнит ли сайт его список
        # Он замечает, что сайт сгенерировал для него уникальный URL
        # (Тут есть поясняющий текст на этот счет)
        self.fail('Finish the test!')

        # Он переходит по этой ссылке - его список еще здесь
