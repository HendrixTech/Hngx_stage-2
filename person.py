from fastapi import APIRouter, Depends, HTTPException
import schema
from database import get_db
from models import Person
from sqlalchemy.orm import Session


router = APIRouter(tags=['Person'])


@router.post("/api", response_model=schema.Person)
async def add_person(person: schema.CreatePerson, db: Session = Depends(get_db)):
    new_person = Person(
        name=person.name
    )
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


@router.get("/api")
async def get_person(db: Session = Depends(get_db)):
    query = db.query(Person).all()
    return query


@router.get("/api/{user_id}", response_model=schema.Person)
async def get_person_id(user_id: str, db: Session = Depends(get_db)):
    if user_id.isdigit():
        query = db.query(Person).filter(Person.id == user_id).first()
    else:
        query = db.query(Person).filter(Person.name == user_id.lower()).first()

    if query is None:
        raise HTTPException(404, "Resource Not Found")
    query = db.query(Person).filter(Person.id == user_id).first()
    return query


@router.patch("/api/{user_id}", response_model=schema.Person)
def update_person(
        user_id: str,
        person_update: schema.Person,
        db: Session = Depends(get_db)
):
    if user_id.isdigit():
        query = db.query(Person).filter(Person.id == user_id).first()
    else:
        query = db.query(Person).filter(Person.name == user_id.lower()).first()

    if query is None:
        raise HTTPException(404, "Resource Npt Found")

    query.name = person_update.name

    db.commit()
    db.refresh(query)

    return query


@router.delete("/api/{user_id}")
async def delete_person(
        user_id: str,
        db: Session = Depends(get_db)
):
    if user_id.isdigit():
        query = db.query(Person).filter(Person.id == user_id).first()
    else:
        query = db.query(Person).filter(Person.name == user_id.lower()).first()

    if query is None:
        raise HTTPException(404, "Resource Not Found")

    db.delete(query)
    db.commit()

    return {f'User {user_id} has been deleted successfully'}


# @router.get('/api/{user_id}', status_code=200, response_model=schemas.Person)
# def get_person_by_id(
#         user_id: str,
#         db: Session = Depends(get_db)
# ):
#     if user_id.isdigit():
#         query = db.query(Person).filter(Person.id == user_id).first()
#     else:
#         query = db.query(Person).filter(Person.name == user_id.lower()).first()
#
#     if query is None:
#         raise HTTPException(404, "Resource Not Found")
#
#     return query
