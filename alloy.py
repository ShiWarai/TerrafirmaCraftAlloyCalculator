from typing import Dict


class Alloy:
    def __init__(self, name: str = None, composition: Dict[str, tuple[int, int]] = {}):
        self.name = name
        self.composition = composition

    def generate_proportion(self, materials_unit: list[int], req_quantity: int) -> list[int]:
        return [10] * len(self.composition)

    def __str__(self):
        if self.name is None:
            return "<неизвестный>"
        else:
            return self.name


BUILTIN_ALLOYS: list[Alloy] \
    = [Alloy("бронза", {"медь": (88, 92), "олово": (8, 12)}),
       Alloy("висмутовая бронза", {"медь": (50, 65), "цинк": (20, 30), "висмут": (10, 20)})]
