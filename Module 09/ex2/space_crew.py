from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Enum defining the hierarchy of space crew ranks."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model representing an individual space crew member."""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    spec: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Model representing a space mission and its assigned crew."""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        """Validates mission constraints across the nested crew data."""
        # Rule 1: Mission ID must start with 'M'
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2: Must have at least one Commander or Captain
        valid_leaders = (Rank.COMMANDER, Rank.CAPTAIN)
        has_leader = any(member.rank in valid_leaders for member in self.crew)
        if not has_leader:
            raise ValueError("Mission needs at least one Commander or Captain")

        # Rule 3: Long missions (> 365 days) need 50% experienced crew
        if self.duration_days > 365:
            exp_count = sum(1 for m in self.crew if m.years_experience >= 5)
            if (exp_count / len(self.crew)) < 0.5:
                raise ValueError("Long missions need 50% experienced crew")

        # Rule 4: All crew members must be active
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Demonstrates nested validation of the SpaceMission model."""
    print("Space Mission Crew Validation")
    print("=========================================")

    # Creating valid crew members
    commander = CrewMember(
        member_id="SC001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        spec="Mission Command",
        years_experience=15
    )

    lieutenant = CrewMember(
        member_id="JS002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=32,
        spec="Navigation",
        years_experience=8
    )

    officer = CrewMember(
        member_id="AJ002",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=28,
        spec="Engineering",
        years_experience=3
    )

    # Creating a valid mission
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[commander, lieutenant, officer],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"{member.name} ({member.rank.value}) - {member.spec}")
        print()
    except ValidationError as e:
        print(f"Error: {e}")

    print("=========================================")
    # Testing an invalid mission (Failing Rule 2: No leader)
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Outpost",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=[officer],  # Invalid: 'officer' is not a commander/captain
            budget_millions=500.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error.get("msg", "Unknown error")
            if "Value error, " in msg:
                msg = msg.replace("Value error, ", "")
            print(f"- {msg}")


if __name__ == "__main__":
    main()
