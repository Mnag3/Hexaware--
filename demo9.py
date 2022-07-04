class employee :
    def __init__(self):
        print("hi constructor............");

    def __abc__(self):
        print("hello method..........");

e=employee();
e.abc();
