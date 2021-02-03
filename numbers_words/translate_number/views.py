from django.shortcuts import render
from .models import Number_word
from .forms import Number_word_form
from .functions import NoteSum
from django.http import HttpResponseRedirect


def index(request):
    # За обработку главной страницы будет отвечать одна функция
    # Если мы получаем POST запрос, то обрабатываем его и проверяем валидность формы
    if request.method == "POST":
        form = Number_word_form(request.POST)
        if form.is_valid():
            # Если форма валидна, создаем экземпляр класса NoteSum
            form_data = form.cleaned_data
            note = NoteSum(form_data['number'], form_data['nds'], form_data['nds_sum'])
            note.number_to_words()  # Вызываем метод парсинга на строковую сумму
            note.create_note_bd()  # Делаем запись в БД
            return HttpResponseRedirect('/')  # Перенаправляем на главную
    form = Number_word_form()
    # Если POST не поступал создаем форму и передаем переменную на страницу
    context = {
        'form': form
    }
    numbers_list = Number_word.objects.order_by('-id')[:40]  # Листинг из БД с ограничением 40 записей
    return render(request, 'translate_number/index.html', locals())
