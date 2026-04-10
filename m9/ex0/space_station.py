from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)  # ge=greater or equal le=less or equal
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    def show_info(self) -> None:
        print(
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Tiempo: {self.last_maintenance.ctime()}\n"
            f"Status: "
            f"{'Operational' if self.is_operational else 'Not operational'}\n"
        )


def main() -> None:
    print("Space Station Data Validation")

    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="All systems nominal"
        )
        print("=" * 40)
        print("Valid station created:")
        valid_station.show_info()

        print("=" * 40)
        print("Expected validation error:")
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None
        )
        invalid_station.show_info()
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
