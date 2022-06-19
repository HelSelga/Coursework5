from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Skill:
    name: str
    stamina: int
    damage: int


fury_punch = Skill(name="Свирепый пинок", stamina=6, damage=12)
hard_shot = Skill(name="Мощный укол", stamina=5, damage=15)
