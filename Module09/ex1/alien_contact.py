from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ValidationException(Exception):
    ...


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(strict=True, min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(strict=True, min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(strict=True, ge=0.0, le=10.0)
    duration_minutes: int = Field(strict=True, ge=1, le=1440)
    witness_count: int = Field(strict=True, ge=1, le=100)
    message_recieved: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(strict=True, default=False)

    @model_validator(mode='after')
    def validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValidationException("contact_id must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValidationException("Physical contacts must be verified")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValidationException("Telepathic contacts must have at least"
                                      " three witnesses")
        if self.signal_strength > 7.0 and not self.message_recieved:
            raise ValidationException("Strong signals must have a message")

        return self


if __name__ == "__main__":
    try:
        ac = AlienContact(
            contact_id="AC_fbusb",
            timestamp=datetime.now(),
            location="42 Lyon",
            contact_type="physical",
            signal_strength=8.5,
            duration_minutes=543,
            witness_count=8,
            is_verified=True,
            message_recieved="test"
        )
        print("Alien Contact Log Validation")
        print("="*35)
        print(f"""Valid contact report:
ID: {ac.contact_id},
Type: {ac.contact_type.value}
Location: {ac.location}
Signal: {ac.signal_strength}/10
Duration: {ac.duration_minutes} minutes
Witnesses: {ac.witness_count}
{f'Message: {ac.message_recieved}' if ac.message_recieved else ''}""")

        print()
        print("="*35)
        print("Expected validation error:")
        AlienContact(
            contact_id="test",
            timestamp=datetime.now(),
            location="Test",
            contact_type=ContactType.RADIO,
            signal_strength=9.0,
            duration_minutes=1,
            witness_count=1,
            is_verified=False
        )
    except Exception as e:
        print(f"Error catched: {e}")
