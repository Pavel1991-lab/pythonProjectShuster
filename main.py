from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',)
def page_index():

    page_content = """ 
    <h1><strong>Бернд Шустер</strong></h1>
    <p><strong>Бе́рнд Шу́стер</strong> (нем. Bernd Schuster; род. 22 декабря 1959[1], Аугсбург, Бавария) — немецкий футбольный тренер,<br> 
    в прошлом профессиональный футболист. Выступал на позиции полузащитника.<br>
    Наиболее известен по выступлениям за испанскую «Барселону».<br>
   <em>Чемпион Европы 1980 года в составе сборной ФРГ, трёхкратный чемпион Испании, 6-кратный обладатель Кубка Испании.<br> 
    Один из лучших футболистов Европы 1980, 1981 и 1985 годов по версии журнала «France Football».</em></p>
    <p><a href = "https://en.wikipedia.org/wiki/Bernd_Schuster">Википедия</a></p>
    """
    return page_content

app.run()
