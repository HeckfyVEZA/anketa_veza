import streamlit as st
pwpw = "kzdytbnxxssypkyo"
st.set_page_config(layout="wide")
import smtplib
def send_email(message):
    sender = 'vevevedflgh@gmail.com'
    password = pwpw

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)
    except Exception as ex:
        st.write(ex)
from datetime import datetime as dtm
import pandas as pd
import streamlit.components.v1 as components
# components.iframe("https://docs.streamlit.io/en/latest")

st.session_state['date'] = dtm.today().strftime('%d.%m.%Y')
st.write(st.session_state['date'])
st.markdown('<p style="font-size:48px; color:#26822F"><b>АНКЕТА ПОСЕТИТЕЛЯ ВЫСТАВКИ</b></p>', unsafe_allow_html=True)
heads = ('«Армия-2023»', '«Нева-2023» ')
hcol = st.columns(6)
with hcol[0]:
    st.header(heads[0])
with hcol[-1]:
    st.image('https://i.postimg.cc/15MjB7kJ/image.png')
st.session_state['Заполнил'] = st.text_input('Заполнил')
st.markdown('---')
# st.markdown('<p style="font-size:598px">ТЕКСТ</p>', unsafe_allow_html=True)
st.header('Основная информация')
cols_1 = st.columns(2)
with cols_1[0]:
    st.session_state['Компания'] = st.text_input('Компания')
    st.session_state['ФИО'] = st.text_input('ФИО')
    st.session_state['Должность'] = st.text_input('Должность')
with cols_1[1]:
    st.session_state['Адрес'] = st.text_input('Адрес')
    st.session_state['Тел./Факс'] = st.text_input('Тел./Факс')
    st.session_state['E-mail'] = st.text_input('E-mail')
st.session_state['Официальный партнер ВЕЗА'] = st.checkbox('Официальный партнер ВЕЗА')
st.session_state['Клиент партнера ВЕЗА'] = st.checkbox('Клиент партнера ВЕЗА')
if st.session_state['Клиент партнера ВЕЗА']:
    st.session_state['Клиент партнера ВЕЗА info'] = st.text_input('Указать компанию')
st.session_state['Первичное знакомство'] = st.checkbox('Первичное знакомство')
st.session_state['Использование продукции ВЕЗА'] = st.checkbox('Использование продукции ВЕЗА')
st.session_state['Также/или использование другой продукции'] = st.checkbox('Также/или использование другой продукции')
if st.session_state['Также/или использование другой продукции']:
    st.session_state['Также/или использование другой продукции info'] = st.text_input('Указать марку производителя')
st.session_state['Основные цели посещения стенда ВЕЗА'] = st.text_area('Основные цели посещения стенда ВЕЗА'.upper())
st.markdown('---')
st.header('Вид деятельности организации:')
cols_2 = st.columns(2)
with cols_2[0]:
    st.session_state['Производство/ОЕМ производство'] = st.checkbox('Производство/ОЕМ производство')
    st.session_state['ЕРС контрактер'] = st.checkbox('ЕРС контрактер')
    st.session_state['Проектная деятельность'] = st.checkbox('Проектная деятельность')
    st.session_state['Монтаж оборудования и пуск в эксплуатацию'] = st.checkbox('Монтаж оборудования и пуск в эксплуатацию')
with cols_2[1]:
    st.session_state['Эксплуатация и обслуживание'] = st.checkbox('Эксплуатация и обслуживание')
    st.session_state['Инжиниринг/Системная интеграция'] = st.checkbox('Инжиниринг/Системная интеграция')
    st.session_state['Дистрибьюция/Проектные поставки'] = st.checkbox('Дистрибьюция/Проектные поставки')
    st.session_state['Другое Вид деятельности организации:'] = st.checkbox('Другое')
    if st.session_state['Другое Вид деятельности организации:']:
        st.session_state['Другое Вид деятельности организации: info'] = st.text_input('Опишите вид деятельности')
st.markdown('---')
st.header('Отрасль:')
cols_3 = st.columns(2)
with cols_3[0]:
    st.session_state['Нефтедобыча/Нефтепереработка'] = st.checkbox('Нефтедобыча/Нефтепереработка')
    st.session_state['Газодобыча/Газопереработка'] = st.checkbox('Газодобыча/Газопереработка')
    st.session_state['Химия/Нефтехимия'] = st.checkbox('Химия/Нефтехимия')
    st.session_state['Энергетика/Атомная энергетика'] = st.checkbox('Энергетика/Атомная энергетика')
    st.session_state['Отопление, вентиляция и кондиционирование'] = st.checkbox('Отопление, вентиляция и кондиционирование')
    st.session_state['Электроника/Полупроводники'] = st.checkbox('Электроника/Полупроводники')
with cols_3[1]:
    st.session_state['Фармацевтика'] = st.checkbox('Фармацевтика')
    st.session_state['Пищевая промышленность'] = st.checkbox('Пищевая промышленность')
    st.session_state['Металлургия'] = st.checkbox('Металлургия')
    st.session_state['Машиностроение'] = st.checkbox('Машиностроение')
    st.session_state['Водоочистка/Водоподготовка'] = st.checkbox('Водоочистка/Водоподготовка')
    st.session_state['Другое Отрасль:'] = st.checkbox('Другoе')
    if st.session_state['Другое Отрасль:']:
        st.session_state['Другое Отрасль: info'] = st.text_input('Опишите отрасль')
st.markdown('---')
st.header('Интерес к продукции ВЕЗА:')
cols_4 = st.columns(2)
with cols_4[0]:
    st.session_state['Вентиляторы'] = st.checkbox('Вентиляторы')
    st.session_state['Воздухообрабатывающие вентиляционные агрегаты'] = st.checkbox('Воздухообрабатывающие вентиляционные агрегаты')
    st.session_state['Клапаны и сетевые элементы'] = st.checkbox('Клапаны и сетевые элементы')
    st.session_state['Канальное оборудование'] = st.checkbox('Канальное оборудование')
    st.session_state['Холодильное оборудование'] = st.checkbox('Холодильное оборудование')
with cols_4[1]:
    st.session_state['Люки и зенитные фонари'] = st.checkbox('Люки и зенитные фонари')
    st.session_state['Отопительное оборудование'] = st.checkbox('Отопительное оборудование')
    st.session_state['Теплоэнергетическое оборудование'] = st.checkbox('Теплоэнергетическое оборудование')
    st.session_state['Автоматика'] = st.checkbox('Автоматика')
st.markdown('---')
galochka = st.columns(3)
with galochka[0]:
    st.markdown('<p style="color:#26822F"><b>Отправить печатный технический каталог?</b></p>', unsafe_allow_html=True)
with galochka[1]:
    st.session_state["Отправить ПЕЧАТНЫЙ ТЕХНИЧЕСКИЙ КАТАЛОГ?"] = st.checkbox(' ')
st.markdown('---')
st.header('Передать подразделению')
departments = ['Отдел продаж департамента региональных отношений','Белгород','Брянск','Верхневолжский регион','Владимир','Владивосток','Волгоград','Воронеж','Екатеринбург','Казань','Киров','Краснодар','Красноярск','Москва','Нижний Новгород','Новосибирск','Омск','Пенза','Пермь','Ростов-на-Дону','Самара','Саранск','Саратов','Тверь','Тюмень','Уфа','Хабаровск','Чебоксары','Челябинск','Чехов','Ярославль','Алматы','Нур-Султан','Беларусь','Ташкент','Санкт-Петербург']
e_mails_of_departments = ['region@veza.ru','belgorod@veza.ru','bcom@veza.ru','vv@veza.ru','vv@veza.ru','vladivostok@veza.ru','volgograd@veza.ru','voronezh@veza.ru','Ekaterinburg@veza.ru','kazan@veza.ru','kirov@veza.ru','krasnodar@veza.ru','krasnoyarsk@veza.ru','msk@veza.ru','nnov@veza.ru','novosibirsk@veza.ru','omsk@veza.ru','penza@veza.ru','perm@veza.ru','rostov@veza.ru','samara@veza.ru','saransk@veza.ru','saratov@veza.ru','tver@veza.ru','tumen@veza.ru','ufa@veza.ru','khabarovsk@veza.ru','cheboksary@veza.ru','chelyabinsk@veza.ru','chehov@veza.ru','vv@veza.ru','astana@veza.ru','astana@veza.ru','office@veza.by','tashkent@veza.ru','spb@veza.ru']
dep_dict = {departments[i]:e_mails_of_departments[i] for i in range(len(departments))}
st.session_state['Подразделение'] = st.selectbox('Подразделение', options=tuple(sorted(departments)), index=14)
st.session_state['Подразделение мыло'] = dep_dict[st.session_state['Подразделение']]
st.write('Как хотите получить обратную связь?')
st.session_state['Письмо'] = st.checkbox('Письмо')
st.session_state['Звонок'] = st.checkbox('Звонок')
st.session_state['Встреча'] = st.checkbox('Встреча')
st.session_state['Приоритет обработки'] = st.radio('Приоритет обработки', options=('A', 'B', "C"), horizontal=True)
# name = jsons_ankets/here_comes_jsons.txt

def write_json(new_data, file_name):
    import pandas as pd
    new_data = str({key:{0:new_data[key]} for key in new_data.keys()})
    st.write(new_data)
    # pd.DataFrame(new_data).to_excel(f"{file_name}.xlsx", index=False)
    # python object to be appended
    send_email(new_data)

def json_click():
    write_json(dict(st.session_state), f'{"_".join(st.session_state["ФИО"].split())}_{"_".join(st.session_state["Компания"].split())}')
    import time
    time.sleep(1)
    from streamlit_js_eval import streamlit_js_eval
    # streamlit_js_eval(js_expressions="parent.window.location.reload()")
st.button("Отправить", on_click=json_click)

