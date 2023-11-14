class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def insert_into_hash_table(employee_dict, employee):
    age = employee.age
    if age in employee_dict:
        employee_dict[age].append(employee)
    else:
        employee_dict[age] = [employee]

def search_employee(employee_dict, emp_id):
    for age, employees in employee_dict.items():
        for employee in employees:
            if employee.emp_id == emp_id:
                return employee
    return None

def average_salary_between_ages(employee_dict, age_min, age_max):
    total_salary = 0
    count = 0
    for age in range(age_min, age_max + 1):
        if age in employee_dict:
            employees = employee_dict[age]
            for employee in employees:
                total_salary += employee.salary
                count += 1
    return total_salary / count if count > 0 else 0

if __name__ == '__main__':
    employee_dict = {}

    N = int(input("Enter the number of employees: "))
    for _ in range(N):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        salary = float(input("Enter Employee Salary: "))
        employee = Employee(emp_id, name, age, salary)
        insert_into_hash_table(employee_dict, employee)

    while True:
        print("\n1. Search for an Employee")
        print("2. Calculate Average Salary between ages 22 and 25")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp_id = int(input("Enter the Employee ID to search: "))
            employee = search_employee(employee_dict, emp_id)
            if employee:
                print(f"Employee ID: {employee.emp_id}")
                print(f"Name: {employee.name}")
                print(f"Age: {employee.age}")
                print(f"Salary: {employee.salary}")
            else:
                print("Employee not found.")

        elif choice == 2:
            average = average_salary_between_ages(employee_dict, 22, 25)
            print(f"Average Salary between ages 22 and 25: {average:.2f}")

        elif choice == 3:
            break
