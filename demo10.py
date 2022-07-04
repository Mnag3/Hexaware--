class employee :
    def __init__(self):
        self.uid= input("enter id :");
        self.name= input("enter name :");
        self.age= input("enter age :");
        self.salary= input("enter salary :");
        self.designation= input("enter designation :");


    def display(self):
        print("id :",self.uid);
        print("name :",self.name);
        print("age :",self.age);
        print("salary :",self.salary);
        print("designation :",self.designation);


e=employee();
e.display();
