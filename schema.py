from pydantic import BaseModel
from datetime import datetime


class CreatePerson(BaseModel):
    name: str


class Person(CreatePerson):
    id: int
    date_created: datetime
    last_updated: datetime
