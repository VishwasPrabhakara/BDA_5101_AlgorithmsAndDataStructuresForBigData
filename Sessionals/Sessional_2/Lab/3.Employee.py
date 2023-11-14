class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        self.left = None
        self.right = None

def insert_employee(root, employee):
    if root is None:
        return employee
    if employee.emp_id < root.emp_id:
        root.left = insert_employee(root.left, employee)
    else:
        root.right = insert_employee(root.right, employee)
    return root

def search_employee(root, emp_id):
    if root is None or root.emp_id == emp_id:
        return root
    if emp_id < root.emp_id:
        return search_employee(root.left, emp_id)
    return search_employee(root.right, emp_id)

def average_salary_between_ages(root, age_min, age_max):
    def inorder_traversal(node):
        if node:
            if age_min <= node.age <= age_max:
                total_salary[0] += node.salary
                count[0] += 1
            inorder_traversal(node.left)
            inorder_traversal(node.right)

    total_salary = [0]
    count = [0]
    inorder_traversal(root)
    return total_salary[0] / count[0] if count[0] > 0 else 0

if __name__ == '__main__':
    root = None

    N = int(input("Enter the number of employees: "))
    for _ in range(N):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        salary = float(input("Enter Employee Salary: "))
        employee = Employee(emp_id, name, age, salary)
        root = insert_employee(root, employee)

    while True:
        print("\n1. Search for an Employee")
        print("2. Calculate Average Salary between ages 20 and 25")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            emp_id = int(input("Enter the Employee ID to search: "))
            employee = search_employee(root, emp_id)
            if employee:
                print(f"Employee ID: {employee.emp_id}")
                print(f"Name: {employee.name}")
                print(f"Age: {employee.age}")
                print(f"Salary: {employee.salary}")
            else:
                print("Employee not found.")

        elif choice == 2:
            average = average_salary_between_ages(root, 20, 25)
            print(f"Average Salary between ages 20 and 25: {average:.2f}")

        elif choice == 3:
            break
