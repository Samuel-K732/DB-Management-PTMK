from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Employee
import sys
from datetime import datetime
from db_manager import DBManager
from data_generator import EmployeeGenerator

engine = create_engine("sqlite:///staff.db")

Session = sessionmaker(bind=engine)

mode = sys.argv[1]

if mode == "1":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

elif mode == "2":
    full_name = sys.argv[2]
    birth_date = sys.argv[3]
    gender = sys.argv[4]

    formatted_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

    with Session() as session:
        employee = Employee(
            full_name=full_name,
            birth_date=formatted_birth_date,
            gender=gender
        )

        db = DBManager(session)
        db.insert(employee)

        print(f"Сотрудник {employee.full_name} был успешно добавлен в базу данных\n"
              f"Возраст сотрудника: {db.get_age(employee.birth_date)} лет")


elif mode == "3":
    with Session() as session:
        db = DBManager(session)
        unique_employees = db.get_unique_employees()

        for member in unique_employees:
            print(f"ФИО: {member.full_name}, "
                  f"Дата рождения: {member.birth_date}, "
                  f"Пол: {member.gender}, "
                  f"Возраст: {db.get_age(member.birth_date)} лет")

elif mode == "4":
    with Session() as session:
        generator = EmployeeGenerator(session)
        db = DBManager(session)

        employees = generator.generate_employees(1000000)
        f_males = generator.generate_f_males(100)
        total = employees + f_males

        db.batch_insert(total)
        print("Было успешно добавлено 1 000 100 записей")

elif mode == "5":
    with Session() as session:
        db = DBManager(session)
        result, duration = db.get_f_males()
        for member in result:
            print(f"ФИО: {member.full_name}, "
                  f"Дата рождения: {member.birth_date}, "
                  f"Пол: {member.gender}")
        print(f"Время выполнения запроса составило {duration:4f} секунд")

elif mode == "6":
    with Session() as session:
        if answer := input("Вы действительно хотите удалить "
                           "все данные из таблицы сотрудников?\n(y/n): ").lower() == "y":
            session.query(Employee).delete()
            session.commit()
            print("Данные удалены")
        else:
            print("Отмена удаления")
