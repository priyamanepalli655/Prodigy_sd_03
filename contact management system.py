employee contact: "
        
        employee = Employee( name, emailid, contact)
        self.employees[id] = employee
        print("Employee added successfully!")

    def view_employees(self):
        if not self.employees:
            print("No employees in the system.")
            return
        
        for id, employee in self.employees.items():
            print(f"Name: {employee.name}")
            print(f"emailid: {employee.emailid}")
            print(f"contact: {employee.contact}")
            print("------------------------")

    def update_employee(self):
        
        employee = self.employees[id]
        print("Enter new details (leave blank to keep current value):")
        
        name = input(f"Name ({employclass Employee:})
    def __init__(self, name, emailid, contact):
        self.name = name
        self.emailid = emailid
        self.contact = contact

class ManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):

        name = input("Enter employee name: ")
        emailid = input("Enter employee emailid: ")
        contact = int(input("Enter ee.name}): ")
        if name:
            employee.name = name
        
        emailid = input(f"emailid ({employee.position}): ")
        if emailid:
            employee.emailid1 = emailid
        
        salary = input(f"contact({employee.contact}): ")
        if contact:
            employee.salary = int(contact)
        
        print("Employee updated successfully!")

    def delete_employee(self):
        id = input("Enter employee ID: ")
        if id not in self.employees:
            print("Employee not found.")
            return
        
        del self.employees[id]
        print("Employee deleted successfully!")

def main():
    management_system = ManagementSystem()
    
    while True:
        print("Simple Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            management_system.add_employee()
        elif choice == "2":
            management_system.view_employees()
        elif choice == "3":
            management_system.update_employee()
        elif choice == "4":
            management_system.delete_employee()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()