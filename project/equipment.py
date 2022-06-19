from dataclasses import dataclass
from typing import List
from random import uniform


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]

    def get_weapon(self, weapon_name: str) -> Weapon:
        for weapon in self.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name: str) -> Armor:
        for armor in self.armors:
            if armor.name == armor_name:
                return armor
        return None

    @property
    def get_weapons_names(self) -> List[str]:
        return [weapon.name for weapon in self.weapons]

    @property
    def get_armors_names(self) -> List[str]:
        return [armor.name for armor in self.armors]
