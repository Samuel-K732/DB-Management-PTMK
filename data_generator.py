import random
import string
from datetime import datetime, timedelta
from models import Employee


class EmployeeGenerator:
    def __init__(self, session):
        self.session = session
        self.first_names = ["Ivan", "Jack", "John", "Peter", "Samuel"]
        self.middle_names = ["Ivanovich", "Vasilievich", "Petrovich", "Aleksandrovich", "Makarovich"]
        self.letters = string.ascii_uppercase

    def _generate_full_name(self, letter):
        second_name = letter + "".join(random.choices(string.ascii_lowercase, k=5))
        first_name = random.choice(self.first_names)
        middle_name = random.choice(self.middle_names)
        return f"{second_name} {first_name} {middle_name}"

    def _generate_birth_date(self):
        start_date = datetime(1960, 1, 1)
        end_date = datetime(2005, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return (start_date + timedelta(days=random_days)).date()

    def _generate_gender(self):
        return random.choice(["Male", "Female"])

    def generate_employees(self, amount):
        employees = []
        count_per_letter = amount // len(self.letters)
        remainder = amount % len(self.letters)
        for letter in self.letters:
            for _ in range(count_per_letter):
                full_name = self._generate_full_name(letter)
                birth_date = self._generate_birth_date()
                gender = self._generate_gender()
                member = Employee(full_name=full_name, birth_date=birth_date, gender=gender)
                employees.append(member)

        for _ in range(remainder):
            letter = random.choice(self.letters)
            full_name = self._generate_full_name(letter)
            birth_date = self._generate_birth_date()
            gender = self._generate_gender()
            member = Employee(full_name=full_name, birth_date=birth_date, gender=gender)
            employees.append(member)

        return employees

    def generate_f_males(self, count=100):
        f_males = []
        for _ in range(count):
            full_name = self._generate_full_name("F")
            birth_date = self._generate_birth_date()
            gender = "Male"
            member = Employee(full_name=full_name, birth_date=birth_date, gender=gender)
            f_males.append(member)
        return f_males
