#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.is_flowering = False
        self.is_prize = False

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming = True
        self.is_flowering = True


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str,
        height: int,
        color: str,
        prize_points
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points
        self.is_prize = True


# ==========================
# GARDEN
# =======================
class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants = []
        self.plant_count: int = 0
        self.total_growth: int = 0
        self.regular: int = 0
        self.flowering: int = 0
        self.prize: int = 0

    def add_plant(self, plant: str):
        self.plants = self.plants + [plant]
        self.plant_count += 1

        if plant.is_prize:
            self.prize += 1
        elif plant.is_flowering:
            self.flowering += 1
        else:
            self.regular += 1

        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        i = 0
        while i < self.plant_count:
            self.plants[i].grow()
            self.total_growth += 1
            i += 1

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        i = 0
        while i < self.plant_count:
            plant = self.plants[i]

            if plant.is_prize:
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                    )
            elif plant.is_flowering:
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming)"
                    )
            else:
                print(f"- {plant.name}: {plant.height}cm")
            i += 1


# ===================================
# GARDEN MANAGER
# ========================================
class GardenManager:
    garden_total: int = 0

    class GardenStats:
        @staticmethod
        def show(garden):
            print(
                f"Plants added: {garden.plant_count}, "
                f"Total growth: {garden.total_growth}cm"
                )
            print(
                f"Plant types: {garden.regular} regular, "
                f"{garden.flowering} flowering, {garden.prize} prize flowers"
                )

    def __init__(self):
        self.gardens = []
        self.garden_count = 0

    def add_garden(self, garden):
        self.gardens = self.gardens + [garden]
        self.garden_count += 1
        GardenManager.garden_total += 1

    @staticmethod
    def validate_height(garden):
        valid = True
        i = 0
        while i < garden.plant_count:
            if garden.plants[i].height <= 0:
                valid = False
            i += 1
        print(f"Height validation test: {valid}")

    def calculate_scores(self):
        i = 0
        output = "Garden scores - "

        while i < self.garden_count:
            garden = self.gardens[i]
            score = 0

            if garden.plant_count == 0:
                score = 92
            else:
                j = 0
                while j < garden.plant_count:
                    plant = garden.plants[j]
                    score += plant.height
                    score += 10
                    if plant.is_prize:
                        score += plant.prize_points
                    j += 1

            output += f"{garden.owner}: {score}"

            if i < self.garden_count - 1:
                output += ", "

            i += 1
        print(output)

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.garden_total}")


# ========================
# DEMO
# ================
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager()

    alice = Garden("Alice")
    bob = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()

    alice.grow_all()
    alice.report()

    print()

    GardenManager.GardenStats.show(alice)

    print()

    GardenManager.validate_height(alice)
    manager.calculate_scores()
    GardenManager.create_garden_network()
