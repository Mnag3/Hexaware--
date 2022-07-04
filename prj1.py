class Developer:
    def create(self):
        self.ID= int(input("Enter ID:"))
        self.name=input("Enter name:")
        self.age=int(input("Enter Age"))
        self.salary=int(input("Enter salary:"))
        self.designation=input("Enter Designation:")
    def display(self):
        print("ID :",self.ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("salary :",self.salary)
        print("Designation :",self.designation)
    def raiseSalary(self):
        this.salary=salary+20000
        print('salary :',self.salary)
class Manager:
    def create(self):
        self.ID=int(input("Enter ID:"))
        self.name=input("Enter name:")
        self.age=int(input("Enter Age"))
        self.salary=int(input("Enter salary:"))
        self.designation=input("Enter Designation:")
    def display(self):
        print("ID :",self.ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("salary :",self.salary)
        print("Designation :",self.designation)
    def raiseSalary(self):
        this.salary=salary+20000
        print('salary :',self.salary)
class Clerk:
    def create(self):
        self.ID=int(input("Enter ID:"))
        self.name=input("Enter name:")
        self.age=int(input("Enter Age"))
        self.salary=int(input("Enter salary:"))
        self.designation=input("Enter Designation:")
    def display(self):
        print("ID :",self.ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("salary :",self.salary)
        print("Designation :",self.designation)
    def raiseSalary(self):
        this.salary=salary+20000
        print('salary :',self.salary)
class Tester:
    def create(self):
        self.ID=int(input("Enter ID:"))
        self.name=input("Enter name:")
        self.age=int(input("Enter Age"))
        self.salary=int(input("Enter salary:"))
        self.designation=input("Enter Designation:")
    def display(self):
        print("ID :",self.ID)
        print("Name :",self.name)
        print("Age :",self.age)
        print("salary :",self.salary)
        print("Designation :",self.designation)
    def raiseSalary(self):
        self.salary=self.salary+20000
        print('salary :',self.salary)

print('1. Create ')		
print('2. display ')
print('3. raise salary ')
print('4. exit ')
D=Developer()
M=Manager()
C=Clerk()
T=Tester()
while True:
    n=int(input('enter the number '))
    if n==1:
        print("Enter type of employee you want to create ")
        print("1. Enter the Developer Details")
        print("2. Enter the Manager Details ")
        print("3.Enter the Clerk Details")
        print("4.Enter the Tester Details")
        n1=int(input())
        if n==1:
            D.create()
        elif n==2:
            M.create()
        elif n==3:
            C.create()
        elif n==4:
            T.create()
        else:
            print('exit from create employee')
    elif n==2:
        print('Display all the members details of employees')
        D.display()
        M.display()
        C.display()
        T.display()
    elif n==3:
        D.raiseSalary()
        M.raiseSalary()
        C.raiseSalary()
        T.raiseSalary()
    else:
        print('exit')
