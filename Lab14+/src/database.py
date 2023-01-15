from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from . import models

engine = create_engine('sqlite:///database.db')
session = Session(bind=engine)


def add_type_of_control(name):
    name_toc = session.query(models.Type_of_control).filter(models.Type_of_control.name == name)

    if name_toc.count() != 0:
        return print("Данный вид контроля уже есть в базе данных")

    new_type = models.Type_of_control(
        name=name
    )

    session.add(new_type)
    session.commit()


def add_pulpit(name):
    pulpit = session.query(models.Pulpit).filter(models.Pulpit.name == name)

    if pulpit.count() != 0:
        return print("Данная кафедра уже есть")

    new_pulpit = models.Pulpit(
        name=name
    )
    session.add(new_pulpit)
    session.commit()


def add_discipline(name, lecture, practice, labs, pulpit_id, toc_id):
    pulpits = session.query(models.Pulpit).filter(models.Pulpit.id == pulpit_id)

    types = session.query(models.Type_of_control).filter(models.Type_of_control.id == toc_id)

    new_discipline = models.Discipline(
        name=name,
        lecture=lecture,
        practice=practice,
        labs=labs,
        pulpit_id=pulpit_id,
        type_of_control_id=toc_id
    )
    if pulpits.count() == 0:
        return print(f'Номер кафедры {pulpit_id} не найден')
    elif types.count() == 0:
        return print(f"Данный вид контроля:{toc_id} не найден")

    session.add(new_discipline)
    session.commit()


def all_disciplines():
    result = {}

    disciplines = session.query(models.Discipline).all()

    for discipline in disciplines:
        result[str(discipline.id)] = {
            "name": discipline.name,
            "lecture": discipline.lecture,
            "practice": discipline.practice,
            "labs": discipline.labs
        }
        pulpits = session.query(models.Pulpit).filter(models.Pulpit.id == discipline.pulpit_id)
        for p in pulpits:
            result[str(discipline.id)].update({
                "pulpit_name": p.name
            })
        types = session.query(models.Type_of_control).filter(
            models.Type_of_control.id == discipline.type_of_control_id)
        for t in types:
            result[str(discipline.id)].update({
                "type_name": t.name
            })
    return result


def all_pulpit():
    result = {}
    pulpits = session.query(models.Pulpit).all()

    count = 0
    disciplines = session.query(models.Discipline).all()

    for pulpit in pulpits:
        for discipline in disciplines:
            if discipline.pulpit_id == pulpit.id:
                count += 1

        result[str(pulpit.id)] = {
            "name": pulpit.name,
            "count_disciplines": count
        }
        count = 0

    return result

    # def all_types_of_control():
    #     types = session.query(models.Type_of_control).all()
    #
    #     return {str(i.id): i.title for i in types}
