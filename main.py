from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime, date, time

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()


