from __future__ import annotations

from dataclasses import dataclass
# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#     from unit import BaseUnit


@dataclass
class Skill:
    # user: str = None
    # target: str = None
    name: str
    stamina: float
    damage: float
    # def _is_stamina_enough(self):
    #     return self.user.stamina > self.stamina
    #
    # def use(self, user: BaseUnit, target: BaseUnit) -> str:
    #     """
    #     Проверка, достаточно ли выносливости у игрока для применения умения.
    #     Для вызова скилла везде используем просто use
    #     """
    #     self.user = user
    #     self.target = target
    #     if self._is_stamina_enough:
    #         return self.skill_effect()
    #     return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


fury_punch = Skill(name="Свирепый пинок", stamina=6, damage=12)
hard_shot = Skill(name="Мощный укол", stamina=5, damage=15)
