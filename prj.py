class Clerk:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=25000;
        self.desig="Clerk";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*5/100);
        print("Raised Salary:",new);
    def options(self):
      print("Choose the below Option number to perform the certain task");
      print("1.Create")
      print("2.Display")
      print("3.Raise Salary")
      print("4.exit")

class Manager:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=80000;
        self.desig="Manager";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*20/100);
        print("Raised Salary:",new);
class Tester:
    def create(self):
        self.uid=int(input("enter the id:"))
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=40000;
        self.desig="Tester";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*10/100);
        print("Raised Salary:",new);
class Developer:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=60000;
        self.desig="Developer";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*15/100);
        print("Raised Salary:",new);
c=Clerk();
m=Manager();
t=Tester();
d=Developer();
counter=0;
print("Choose the below Option number to perform the certain task");
print("1.Create");
print("2.Display");
print("3.Raise Salary");
print("4.exit");

while True:
    counter+=1;
    n=int(input("enter your choice number:"));
    if(n==1):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.developer");
        n1=int(input("choose the option number to create:"));
        if(n1==1):
            print("enter the clerk details")
            c.create();
            c.options()
            
            
        elif(n1==2):
            print("enter the Manager details")
            m.create();
            c.options()
            
           
        elif(n1==3):
            print("enter the Tester details")
            t.create();
            c.options()
            
        elif(n1==4):
            print("enter the Developer details")
            d.create();
            c.options()
            
            
        else:
            print("wrong selection......:(");
            
        
    if(n==2):
        c.display();
        m.display();
        t.display();
        d.display();
        c.options()
        
    if(n==3):
        c.raisesalary();
        m.raisesalary();
        t.raisesalary();
        d.raisesalary();
        c.options()
        
    if(n==4):
        print("thank you.....:)");
        break;
