import collections, datetime
from django.shortcuts import render, render_to_response

# Create your views here.
pages_l = [
    {'id': 'info',
    'url': '',                                                                              # Вопрос #1.
    'tag': 'Info',
    'cap': 'Инфо',
    'data':{
        'fio':      {'tag':'Имя',           'val':'Андрей Квичанский'},
        'foto':     {'tag':'Фото',          'val':'img/kv_585x643.jpg'},                        # Вопрос #7.
        # 'foto':   {'tag':'Фото',          'val':'static/img/kv_585x643.jpg'},               # Вопрос #1.
        'b_date':   {'tag':'Год рождения',  'val': datetime.datetime(1965, 5, 23)},
        'age':      {'tag':'Возраст',       'val':'51 год'},
        'edu':      {'tag':'Образование',   'val':'Высшее, МГУ 1982-1987, мехмат'},
        'prof':     {'tag':'Профессия',     'val':'Программист с 1987 года'},
        'mail':     {'tag':'Почта',         'val':'kvichans@mail.ru'},
        },
    },
    {'id': 'edu',
    'url': 'edu',
    'tag': 'Education',
    'cap': 'Учеба',
    'data':[
        {'what': 'Школа',
         'html': 'Физ.-мат. <a href="http://www.fml31.ru/">лицей № 31</a>, г. Челябинск'    # Вопрос #5.
         },
        {'what': 'Вуз',
         'html': '<a href="http://www.math.msu.ru/">МГУ, мехмат</a>, специализация "Алгебра"'
         },
        ],
    },
    {'id': 'work',
    'url': 'work',
    'tag': 'Employment',
    'cap': 'Работа',
    'data':[
        {'where':'ВННИФТ г. Снежинск (бывший Челябинск-70)',
         'info':[
             ('Период', '1987-2000'),
             ('Должности', 'МНС, НС, СНС'),
             ('Языки', 'ФОРТРАН, C++, Эль-76'),
             ('Награды',
              'Премия имени А.А.Бунатяна в области математики и вычислительной техники "Лучший молодой специалист 2000 года"'),
         ]},
        {'where': 'Компания "НейрОК"',
         'info': [
             ('Период', '1998-2003'),
             ('Должности', 'Главный технолог, Главный инженер в группе из 10 программистов'),
             ('Языки', 'Java, C++, Matlab, Visual Basic, VBA, XML, XSL, JavaScript, Python'),
         ]},
        {'where': 'Компания "Смета-Багира"',
         'info': [
             ('Период', '2003-'),
             ('Должности', 'СНС'),
             ('Языки', 'Visual FoxPro, VBA'),
         ]},
        {'where': 'Open source',
         'info': [
             ('Период', '2012-'),
             ('Проекты', '''<a href="http://www.uvviewsoft.com/synwrite/">SynWrite</a>,
                            <a href="http://www.uvviewsoft.com/cudatext/">CudaText</a>'''),
             ('Вклад', '''Тестирование, Новые идеи, Разработка плагинов
                        (5 плагинов для SynWrite,
                        12 <a href="https://sourceforge.net/projects/kvichans-plugins/files/cudatext-addons/">плагинов</a> для CudaText)'''),
             ('Языки', 'Python, JSON'),
         ]},
        ],
    },
    {'id': 'joi',
    'url': 'joi',
    'tag': 'Hobby',
    'cap': 'Увлечения',
    'data':[
        {'what':'Игра Го',
         'html':'''История рейтинга на сервере
                <a href="http://www.dragongoserver.net/userinfo.php?uid=83477">DGS</a><br>
                <img width="25%" height="25%" src="/static/img/dgs-graph.PNG" alt="История рейтинга">'''    # Вопросы #5. #7.
         },
        {'what':'Новая Хронология',
         'html':'<a href="http://chronologia.org/">Сайт</a> проекта Новая Хронология'
         },
        ],
    },
]
pages = collections.OrderedDict([(p['id'], p) for p in pages_l])

def main(request):
    cntx = {'the_page': pages['info'],
            'pages': pages,
            }
    return render_to_response("info.html", cntx)

def edu(request):
    cntx = {'the_page': pages['edu'],
            'pages': pages,
            }
    return render_to_response("edu.html", cntx)

def work(request):
    cntx = {'the_page': pages['work'],
            'pages': pages,
            }
    return render_to_response("work.html", cntx)

def hobby(request):
    cntx = {'the_page': pages['joi'],
            'pages': pages,
            }
    return render_to_response("joi.html", cntx)

# Вопросы:
#1. Про разделение слоев:
    # Как вынести в конфиг.структуру (см pages) адреса, не разрушая разделение функций между views.py и urls.py?
    # Как вынести в конфиг.структуру (см pages) ссылки на картинки

#2. Про использование контекста в шаблоне:
    # Как при вставке из контекста {{ dt.par }} брать значение par тоже из контекста?
    # Например, dt={'a':1, 'b':2}, par='b' и нужно вставить dt['b']

#3. Перекрытие контекст-переменных:
    # Есть контекст={'name':1, 'names:{'name':2}}
    # Что вставится при
    #   {%for name,num in names.items %}
    #       {{name}}
    #   {% endfor %}

#4. Есть ли способ извлекать из list или dict контекста,
    # указывая умолчательное значение,
    # то есть аналог {}.get('key', 'def_val') ?

#5. Нормально ли хранить размеченные данные? См
#       Физ.-мат. <a href="http://www.fml31.ru/">лицей № 31</a>

#6. Будут ли отрабатывать dj-теги {% %} внутри html-комментариев? Ответ: да

#7. Как продолжить работу шаблонизатора на вставленном из контекста значении?

#8. Можно ли поместить {% load static from staticfiles %} в базовый шаблон?