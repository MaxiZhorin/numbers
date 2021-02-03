from django.test import TestCase
from .functions import NoteSum
from .models import Number_word
from django.test import Client


class FunctionsTestCase(TestCase):
    def test_index(self):
        # Тестирум создание записи через функцию и через POST.
        test_note = NoteSum(123, False, 20)
        test = test_note.create_note_bd()
        c = Client()
        response = c.post('', {'number': 123, 'nds': 'False', 'nds_sum': 20})
        numbers_list = Number_word.objects.order_by('-id')
        num1 = numbers_list[0]
        num2 = numbers_list[1]
        self.assertEqual(num1.number, num2.number)  # Проверяем что созданы 2 одинаковые записи



    def test_create_db(self):
        # Проверяем запись в БД через класс
        test_note = NoteSum(150181.06, False, 20)
        test = test_note.create_note_bd()
        obj = Number_word.objects.order_by('-id')[0]
        self.assertEqual(test, obj)

    def test_test_translate_number_to_words_no_NDS(self):
        # Проверяем парсинг на правильный вывод без ндс
        test_note = NoteSum(150181.06, False, 20)
        test = test_note.number_to_words()
        result = '150181.06 руб. (сто пятьдесят тысяч сто восемьдесят один) рубль 6 копеек'
        self.assertEqual(test_note.number_str, result)

    def test_translate_number_to_words_NDS(self):
        # Проверяем парсинг на правильный вывод с ндс
        test_note = NoteSum(150181.06, True, 20)
        test = test_note.number_to_words()
        result = '150181.06 руб. (сто пятьдесят тысяч сто восемьдесят один) рубль 6 копеек, включая НДС (20%) в сумме 25030.18 руб. (двадцать пять тысяч тридцать) рублей 18 копеек'
        self.assertEqual(test_note.number_str, result)