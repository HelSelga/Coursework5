from flask import render_template, Flask, request, redirect

from project.classes import unit_classes
from project.unit import BaseUnit
from project.utils import load_equipment

app = Flask(__name__)
app.url_map.strict_slashes = False


heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

EQUIPMENT = load_equipment()

arena =  ... # TODO инициализируем класс арены


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/choose-hero/", methods=["GET", "POST"])
def choose_hero():
    if request.method == "GET":
        return render_template(
            'hero_choosing.html',
            header="Выберите героя",
            classes=unit_classes.values(),
            equipment=EQUIPMENT,
            next_button="Выбрать врага"
        )
    if request.method == "POST":
        ...
    return redirect('/choose-enemy')


@app.route("/choose-enemy/", methods=["GET", "POST"])
def choose_enemy():
    if request.method == "GET":
        return render_template(
            'hero_choosing.html',
            header="Выберите врага",
            classes=unit_classes.values(),
            equipment=EQUIPMENT,
            next_button="Начать сражение"
        )
    if request.method == "POST":
        ...
    return redirect('/fight')



@app.route("/fight/")
def start_fight():
    # TODO выполняем функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    # TODO рендерим экран боя (шаблон fight.html)
    pass


@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (просто рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика практикчески идентична предыдущему эндпоинту
    pass


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    pass


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return render_template("index.html", heroes=heroes)


if __name__ == "__main__":
    app.run()
