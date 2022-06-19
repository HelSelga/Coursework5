from dataclasses import dataclass
from typing import Dict

from skills import Skill, fury_punch, hard_shot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


class WarriorClass(UnitClass):
    name: str = "Воин"
    max_health: float = 60.0
    max_stamina: float = 30.0
    attack: float = 0.8
    stamina: float = 0.9
    armor: float = 1.2
    skill: Skill = fury_punch


class ThiefClass(UnitClass):
    name: str = "Вор"
    max_health: float = 50.0
    max_stamina: float = 25.0
    attack: float = 1.5
    stamina: float = 1.2
    armor: float = 1.0
    skill: Skill = hard_shot


unit_classes: Dict[str, type[UnitClass]] = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
