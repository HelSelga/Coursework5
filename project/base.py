from typing import Optional

from unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    game_results = ''

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> Optional[str]:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            return self._end_game(results='Ничья')
        elif self.player.hp <= 0:
            return self._end_game(results='Игрок проиграл битву')
        elif self.enemy.hp <= 0:
            return self._end_game(results='Игрок выиграл битву')
        else:
            return None

    def _stamina_regeneration(self):
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    def next_turn(self):
        if results := self._check_players_hp():
            return results
        if not self.game_is_running:
            return self.game_results
        dealt_damage: Optional[float] = self.enemy.hit(self.player)
        if dealt_damage is not None:
            self.player.get_damage(dealt_damage)
            results = f"{self.player.name}, пробивает {self.enemy.armor.name} соперника и наносит {dealt_damage} урона."
        else:
            results = f"{self.player.name}, наносит удар, но {self.enemy.armor.name} cоперника его останавливает."
        self._stamina_regeneration()
        return results

    def _end_game(self, results: str):
        self.game_is_running = False
        self._instances = {}
        self.game_results = results
        return results

    def player_hit(self):
        dealt_damage = self.player.hit(self.enemy)
        if dealt_damage is not None:
            self.enemy.get_damage(dealt_damage)
            return f"<p>{self.enemy.name} получает {dealt_damage} урона</p><p>{self.next_turn()}</p>"
        return f"<p>Не хватило выносливости использовать {self.player.weapon.name}</p><p>{self.next_turn()}</p>"

    def player_use_skill(self):
        dealt_damage: Optional[int] = self.player.use_skill()
        if dealt_damage is not None:
            self.enemy.get_damage(dealt_damage)
            return f"<p>Навык {self.player.unit_class.skill.name} использован, нанесено {dealt_damage} урона </p><p>{self.next_turn()}</p>"
        return f"<p>Не хватило выносливости использовать навык<p><p>{self.next_turn()}</p>"
