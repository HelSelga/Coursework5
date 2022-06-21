from functools import wraps
from typing import Dict, Type

from flask import render_template, Flask, request, redirect

from project.base import Arena
from project.classes import unit_classes
from project.unit import BaseUnit, PlayerUnit, EnemyUnit
from project.utils import load_equipment

app = Flask(__name__)
app.url_map.strict_slashes = False

heroes: Dict[str, BaseUnit] = dict()

EQUIPMENT = load_equipment()

arena = Arena()


@app.route("/")
def menu_page():
    return render_template("index.html")


@app.route("/choose-hero/", methods=["GET", "POST"])
def choose_hero():
    if request.method == "GET":
        return render_template(
            "hero_choosing.html",
            header="Выберите героя",
            classes=unit_classes.values(),
            equipment=EQUIPMENT,
            next_button="Выбрать врага"
        )
    heroes["player"] = PlayerUnit(
        unit_class=unit_classes[request.form["unit_class"]],
        weapon=EQUIPMENT.get_weapon(request.form["weapon"]),
        armor=EQUIPMENT.get_armor(request.form["armor"]),
        name=request.form["name"]
    )
    return redirect("/choose-enemy")


@app.route("/choose-enemy/", methods=["GET", "POST"])
def choose_enemy():
    if request.method == "GET":
        return render_template(
            "hero_choosing.html",
            header="Выберите врага",
            classes=unit_classes.values(),
            equipment=EQUIPMENT,
            next_button="Начать сражение"
        )

    if request.method == "POST":
        heroes["enemy"] = EnemyUnit(
            unit_class=unit_classes[request.form["unit_class"]],
            weapon=EQUIPMENT.get_weapon(request.form["weapon"]),
            armor=EQUIPMENT.get_armor(request.form["armor"]),
            name=request.form["name"]
        )
        return redirect("/fight")


@app.route("/fight/")
def start_fight():
    if "player" in heroes and "enemy" in heroes:
        arena.start_game(**heroes)
        return render_template("fight.html", heroes=heroes, result="Бой начался!")
    return redirect("/")


@app.route("/fight/hit")
def hit():
    if arena.game_is_running:
        return render_template("fight.html", heroes=heroes, result=arena.player_hit())
    if arena.game_results:
        return render_template("fight.html", heroes=heroes, result=arena.game_results)
    return redirect("/")


@app.route("/fight/use-skill")
def use_skill():
    if arena.game_is_running:
        return render_template("fight.html", heroes=heroes, result=arena.player_use_skill())
    if arena.game_results:
        return render_template("fight.html", heroes=heroes, result=arena.game_results)
    return redirect("/")


@app.route("/fight/pass-turn")
def pass_turn():
    if arena.game_is_running:
        return render_template("fight.html", heroes=heroes, result=arena.next_turn())
    if arena.game_results:
        return render_template("fight.html", heroes=heroes, result=arena.game_results)
    return redirect("/")


@app.route("/fight/end-fight")
def end_fight():
    return redirect("/")


if __name__ == "__main__":
    app.run()
