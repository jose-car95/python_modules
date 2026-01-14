#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> int:
        shade_radio: int = self.height + (self.trunk_diameter / 2)
        shade_area = 3.14 * shade_radio ** 2
        return f"{self.name} provides {shade_area} square meters of shade"

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        
        return f"{super().get_info()}, {self.harvest_season} harvest"

    def get_nutrition(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    # Flowers
    rose: Flower = Flower("Rose", 25, 30, "red")
    tulip: Flower = Flower("Tulip", 20, 25, "yellow")

    # Trees
    oak: Tree = Tree("Oak", 500, 1825, 50)
    pine: Tree = Tree("Pine", 600, 1500, 45)

    # Vegetables
    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot: Vegetable = Vegetable("Carrot", 30, 70, "autumn", "beta-carotene")

    print(f"{rose.get_info()}")
    print(f"{rose.bloom()}\n")
    
    print(f"{oak.get_info()}")
    print(f"{oak.produce_shade()}\n")
    
    print(f"{tomato.get_info()}")