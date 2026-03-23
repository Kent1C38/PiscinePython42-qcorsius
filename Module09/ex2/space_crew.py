from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class ValidationError(Exception):
    ...


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(strict=True, min_length=3, max_length=10)
    name: str = Field(strict=True, min_length=3, max_length=50)
    rank: Rank = Field(strict=True)
    age: int = Field(strict=True, ge=18, le=80)
    specialization: str = Field(strict=True, min_length=3, max_length=30)
    years_experience: int = Field(strict=True, ge=0, le=50)
    is_active: bool = Field(strict=True, default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(strict=True, min_length=5, max_length=15)
    mission_name: str = Field(strict=True, min_length=3, max_length=100)
    destination: str = Field(strict=True, min_length=3, max_length=50)
    launch_date: datetime = Field(strict=True)
    duration_days: int = Field(strict=True, ge=1, le=3650)
    crew: list[CrewMember] = Field(strict=True, min_length=1, max_length=12)
    mission_status: str = Field(strict=True, default="planned")
    budget_millions: float = Field(strict=True, ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validator(self) -> "SpaceMission":
        if not self.mission_id.startswith('M'):
            raise ValidationError("Mission id should startt with 'M'")
        has_high_graded = False
        for cm in self.crew:
            if cm.rank == Rank.COMMANDER or cm.rank == Rank.CAPTAIN:
                has_high_graded = True
            if not cm.is_active:
                raise ValidationError("All crew members must be active")
        if not has_high_graded:
            raise ValidationError("A Commander or a Captain must be present")

        if self.duration_days > 365:
            experienced_crew = [
                cm for cm in self.crew if cm.years_experience >= 5]
            if len(experienced_crew) < len(self.crew) // 2:
                raise ValidationError("Long missions must have 50% of "
                                      "experienced crew members (5+ years)")

        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("="*35)
    try:
        mission = SpaceMission(
            mission_id="M_MARS01",
            mission_name="Mars Colonisation",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=365,
            crew=[
                CrewMember(
                    member_id="m001",
                    name="Test Commander",
                    rank=Rank.COMMANDER,
                    age=36,
                    specialization="Pilot",
                    years_experience=8
                ),
                CrewMember(
                    member_id="m002",
                    name="Test Cadet",
                    rank=Rank.CADET,
                    age=20,
                    specialization="Assistant",
                    years_experience=0
                )
            ],
            budget_millions=10
        )
        print(f"""Valid mission created:
Mission: {mission.mission_name}
ID: {mission.mission_id}
Destination: {mission.destination}
Duration: {mission.duration_days} days
Budget: ${mission.budget_millions}M
Crew Size: {len(mission.crew)}
Crew Members:""")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")

        print()
        print("="*35)
        print("Expected validation error:")
        SpaceMission(
            mission_id="M1325",
            mission_name="TEST",
            launch_date=datetime.now(),
            destination="Terra",
            duration_days=2,
            crew=[CrewMember(member_id="007", name="kadai", rank=Rank.CADET,
                             age=18, specialization="None",
                             years_experience=0)],
            budget_millions=1
        )
    except Exception as e:
        print(f"Error catched: {e}")
