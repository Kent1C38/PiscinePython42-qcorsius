from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(strict=True, min_length=3, max_length=10)
    name: str = Field(strict=True, min_length=1, max_length=50)
    crew_size: int = Field(strict=True, ge=1, le=20)
    power_level: float = Field(strict=True, ge=0.0, le=100.0)
    oxygen_level: float = Field(strict=True, ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default=None)


try:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2036-04-08T10:00:42Z",
        # is_operational=True,
    )

    print(f"""Space Data Validation
====================================
Valid station created
ID: {station.station_id}
Name: {station.name}
Crew: {station.crew_size} people
Power: {station.power_level}%
Oxygen: {station.oxygen_level}%
Satus: {'Operational' if station.is_operational else 'Defective'}

Last Maintenance: {station.last_maintenance}
{f'Notes: {station.notes}' if station.notes else ''}""")

    print("="*20)
    print("Expected error here...")
    SpaceStation(
        station_id="p",
        name="test",
        crew_size=100,
        power_level=150.0,
        oxygen_level=-3.0,
        last_maintenance=datetime.fromisoformat("2000-01-01"),
        is_operational=False
    )
except Exception as e:
    print(f"Error occured: {e}")
