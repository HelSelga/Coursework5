from __future__ import annotations

import random
from abc import ABC, abstractmethod
from equipment import EquipmentData, Weapon, Armor
from classes import UnitClass
from random import randint
from typing import Optional

base_reuse_stamina = 1


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = self.unit_class.max_health
        self.stamina = self.unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self._is_skill_used = False

    @property
    def health_points(self):
        return round(self.hp, 1)

    @health_points.setter
    def health_points(self, value):
        self.hp = value

    @property
    def stamina_points(self):
        return round(self.stamina, 1)

    @stamina_points.setter
    def stamina_points(self, value):
        self.stamina = value

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    @property
    def total_armor(self):
        if self.stamina - self.armor.stamina_per_turn >= 0:
            return round(self.armor.defence * self.unit_class.armor, 1)
        return 0

    def count_damage(self, target: BaseUnit) -> float:
        if self.stamina - self.weapon.stamina_per_hit < 0:
            return None
        hero_damage = self.weapon.damage * self.unit_class.attack
        dealt_damage = hero_damage - target.total_armor

        if dealt_damage < 0:
            return 0
        self.stamina -= self.weapon.stamina_per_hit
        return round(dealt_damage, 1)

    def get_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def regenerate_stamina(self):
        delta_stamina = base_reuse_stamina * self.unit_class.stamina
        if self.stamina + delta_stamina <= self.unit_class.max_stamina:
            self.stamina += delta_stamina
        else:
            self.stamina = self.unit_class.max_stamina
        return self.stamina

    @abstractmethod
    def hit(self, target: BaseUnit) -> Optional[float]:
        pass

    def use_skill(self) -> Optional[int]:
        if not self._is_skill_used and self.stamina >= self.unit_class.skill.stamina:
            self._is_skill_used = True
            damage = round(self.unit_class.skill.damage, 1)
            return damage
        return None


class PlayerUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> Optional[float]:
        return self.count_damage(target)


class EnemyUnit(BaseUnit):
    def hit(self, target: BaseUnit) -> Optional[float]:
        if randint(0, 100) < 10 and self.stamina >= self.unit_class.skill.stamina and not self._is_skill_used:
            self.use_skill()
        return self.count_damage(target)

