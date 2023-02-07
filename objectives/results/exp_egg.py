from worlds.ff6wc.WorldsCollide.objectives.results._objective_result import *
from worlds.ff6wc.WorldsCollide.data.item_names import name_id as item_name_id

class Field(field_result.Result):
    def src(self):
        return [
            field.AddItem(item_name_id["Exp. Egg"]),
        ]

class Battle(battle_result.Result):
    def src(self):
        return [
            battle_result.AddItem(item_name_id["Exp. Egg"]),
        ]

class Result(ObjectiveResult):
    NAME = "Exp. Egg"
    def __init__(self):
        super().__init__(Field, Battle)
