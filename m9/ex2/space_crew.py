from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(ge=1, le=12)  # De 1 a 12 miembros(crew)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must strat with "M"')

        has_leader: bool = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                member.years_experience >= 5
                for member in self.crew
            )
            required_experienced = len(self.crew) / 2
            if experienced_count < required_experienced:
                raise ValueError(
                    "Long missions need at least 50% experienced crew"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    pass


if __name__ == "__main__":
    main()
