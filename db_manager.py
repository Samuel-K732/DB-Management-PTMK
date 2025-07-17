from models import Employee
from datetime import date
from timer import perf_timer


class DBManager:
    def __init__(self, session):
        self.session = session

    def insert(self, obj):
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)

    def get_age(self, birth_date):
        today = date.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def get_unique_employees(self):
        employees = self.session.query(Employee).order_by(Employee.full_name).all()
        keys = set()
        unique_employees = []
        for member in employees:
            key = (member.full_name, member.birth_date)
            if key not in keys:
                unique_employees.append(member)
                keys.add(key)
        return unique_employees

    def batch_insert(self, employees, batch_size=10000):
        for i in range(0, len(employees), batch_size):
            batch = employees[i:i + batch_size]
            self.session.add_all(batch)
            self.session.commit()

    @perf_timer
    def get_f_males(self):
        return self.session.query(Employee).filter(Employee.gender == "Male", Employee.full_name.startswith("F")).all()
