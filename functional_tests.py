from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        # Удовлетворенный, Коля уходит спать
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Коля услышал о новом крутом приложении для отслеживания задач
        # Он переходит на главную страницу приложения
        self.browser.get('http://localhost:8000')

        # Он видит, что в названии страницы и хэдере упомянуты To-do листы
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Коле предлагают с ходу написать задачу

        # Он вводит "Купить новую кастрюлю на улицу" в текст-бокс
        # (Коля очень бедный и пьет только дождевую воду из кастрюли)

        # Он нажимает Enter, страница обновляется и теперь в 
        # To-do листе есть его запись - 1. "Купить новую кастрюлю на улицу"

        # Текст бокс с приглашением написать еще одну задачу не пропал
        # Коля вводит "Молиться Перуну чтобы пошел дождь" (Коля язычник)

        # Страница снова обновляется и теперь в списке есть две записи

        # Коля гадает, запомнит ли сайт его список
        # Он замечает, что сайт сгенерировал для него уникальный URL
        # (Тут есть поясняющий текст на этот счет)

        # Он переходит по этой ссылке - его список еще здесь
if __name__ == '__main__':
    unittest.main(warnings='ignore')
