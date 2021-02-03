import requests
from bs4 import BeautifulSoup
from .models import Number_word


class NoteSum:

    def __init__(self, number, nds, nds_sum):
        self.number = number
        self.nds = nds
        self.nds_sum = nds_sum
        self.number_str = ''

    def get_sum_str(self, number):
        # Метод парсит стровое значение
        url = 'https://summa-propisyu.ru/?summ=' + str(number) + '&vat=20&val=0&sep=0'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sp = soup.find(id="result11").text
        sp = sp.split(',')[0]
        return sp

    def number_to_words(self):
        if self.nds:  # Проверяем булевое значение на НДС
            sum_nds1 = self.get_sum_str(self.number)  # Получаем сумму прописью
            sum_nds2 = (self.number / (100 + self.nds_sum) * self.nds_sum)  # Вычисляем сумму ндс
            sum_nds2 = self.get_sum_str(round(sum_nds2, 2))
            sum_result = f"{sum_nds1}, включая НДС ({self.nds_sum}%) в сумме {sum_nds2}"
            # Записываем форматированную строку
            self.number_str = sum_result
            return self.number_str
        else:
            # Если флага НДС нет делаем определенную запись
            self.nds_sum = 0
            self.number_str = self.get_sum_str(self.number)
            return self.number_str

    def create_note_bd(self):
        # Делаем запись в БД
        new_note = Number_word()
        new_note.number = self.number
        new_note.nds = self.nds
        new_note.nds_sum = self.nds_sum
        new_note.number_sting = self.number_str
        new_note.save()
        return new_note
