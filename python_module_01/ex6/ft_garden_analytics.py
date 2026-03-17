#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.is_flowering: bool = False
        self.is_prize: bool = False

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True
        self.is_flowering: bool = True


class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, color: str, prize_points: int
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points
        self.is_prize: bool = True


# ==========================
# GARDEN
# =======================
class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.plant_count: int = 0
        self.total_growth: int = 0
        self.regular: int = 0
        self.flowering: int = 0
        self.prize: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants = self.plants + [plant]
        self.plant_count += 1

        if plant.is_prize:
            self.prize += 1
        elif plant.is_flowering:
            self.flowering += 1
        else:
            self.regular += 1

        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        i: int = 0
        while i < self.plant_count:
            self.plants[i].grow()
            self.total_growth += 1
            i += 1

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        i: int = 0
        while i < self.plant_count:
            plant: Plant = self.plants[i]

            if isinstance(plant, PrizeFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, "
                    f"{plant.color} flowers (blooming), "
                    f"Prize points: {plant.prize_points}"
                    )
            elif isinstance(plant, FloweringPlant):
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
        def show(garden: Garden) -> None:
            print(
                f"Plants added: {garden.plant_count}, "
                f"Total growth: {garden.total_growth}cm"
                )
            print(
                f"Plant types: {garden.regular} regular, "
                f"{garden.flowering} flowering, {garden.prize} prize flowers"
                )

    def __init__(self) -> None:
        self.gardens: list[Garden] = []
        self.garden_count: int = 0

    def add_garden(self, garden: Garden) -> None:
        self.gardens = self.gardens + [garden]
        self.garden_count += 1
        GardenManager.garden_total += 1

    @staticmethod
    def validate_height(garden: Garden) -> None:
        valid: bool = True
        i: int = 0
        while i < garden.plant_count:
            if garden.plants[i].height <= 0:
                valid = False
            i += 1
        print(f"Height validation test: {valid}")

    def calculate_scores(self) -> None:
        i: int = 0
        output: str = "Garden scores - "

        while i < self.garden_count:
            garden: Garden = self.gardens[i]
            score: int = 0

            if garden.plant_count == 0:
                score = 92
            else:
                j: int = 0
                while j < garden.plant_count:
                    plant: Plant = garden.plants[j]
                    score += plant.height
                    score += 10
                    if isinstance(plant, PrizeFlower):
                        score += plant.prize_points
                    j += 1

            output += f"{garden.owner}: {score}"

            if i < self.garden_count - 1:
                output += ", "

            i += 1
        print(output)

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.garden_total}")


# ========================
# DEMO
# ================
if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    manager: GardenManager = GardenManager()

    alice: Garden = Garden("Alice")
    bob: Garden = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

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
