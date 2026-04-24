from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """Enum defining the valid types of alien contact."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model representing an alien contact log."""
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        """Validates complex business rules for alien contacts."""
        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Rule 2: Physical contact reports must be verified
        is_physical = self.contact_type == ContactType.PHYSICAL
        if is_physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        is_telepathic = self.contact_type == ContactType.TELEPATHIC
        if is_telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact needs at least 3 witnesses")

        # Rule 4: Strong signals (>7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (>7.0) must include a message")

        return self


def main() -> None:
    """Demonstrates validation of the AlienContact model."""
    print("Alien Contact Log Validation")
    print("======================================")

    # Creating a valid contact report
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'\n")
    except ValidationError as e:
        print(f"Error: {e}")

    print("======================================")
    # Testing an invalid report to trigger validation errors
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=2,  # Invalid: telepathic needs >= 3 witnesses
            is_verified=True
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error.get("msg", "Unknown error")
            # Cleaning the error message formatting for cleaner output
            if "Value error, " in msg:
                msg = msg.replace("Value error, ", "")
            print(f"- {msg}")


if __name__ == "__main__":
    main()
