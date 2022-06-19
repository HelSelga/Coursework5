import json
from typing import Union
import os

import marshmallow_dataclass

from project.equipment import EquipmentData

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
EQUIPMENT_PATH: str = os.path.join(BASE_DIR, 'data', 'equipment.json')


def read_json(file_path: str) -> Union[dict, list]:
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


def load_equipment() -> EquipmentData:
    equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
    return equipment_schema().load(data=read_json(EQUIPMENT_PATH))
