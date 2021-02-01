import requests
from django.shortcuts import render
from .models import Number_word
from bs4 import BeautifulSoup
from .forms import Number_word_form


def get_int_or_float(num):
    sum = num
    if sum.is_integer():
        return int(sum)
    else:
        return round(sum, 2)


def number_to_words(number, nds=False):
    url = 'https://summa-propisyu.ru/?summ=' + str(number) + '&vat=20&val=0&sep=0'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    if nds:
        sp1 = soup.find(id="result11").text
        return sp1
    else:
        print('_____________')
        sp1 = soup.find(id="result3").text
        print(sp1)
        sp1 = sp1.split('рубль')
        sp1 = str(number) + ' (' + sp1[0] + ')' + sp1[1]
        return sp1


def index(request):
    if request.method == "POST":
        form = Number_word_form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_number = get_int_or_float(form_data['number'])
            form_nds = form_data['nds']
            print(form_nds)
            form_number_str = number_to_words(form_number, bool(form_nds))
            # new_note = Number_word()
            # new_note.number = form_number
            # new_note.nds = form_nds
            # new_note.number_sting = form_number_str
            # new_note.save()


            print('fasfsafasfasfasfasfsaf', form_number, form_nds, form_number_str)
            # form.save()
    form = Number_word_form()
    context = {
        'form': form
    }
    numbers_list = Number_word.objects.order_by('-id')
    for i in numbers_list:
        print(i)
    return render(request, 'translate_number/index.html', locals())
