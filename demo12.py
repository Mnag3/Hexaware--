l1=[1,2,3,4,5,6,7,8,9,10];
print(l1);

 


sum=0;
for i in l1:
    sum=sum+i;

 

print("Total :",sum);

 

 

a1=[1,2,3,4,5,6,7,8];
a2=[1,8,10,20,30,40];

 

print(a1==a2)
for i in a1:
    for j in a2:
        if i == j :
            print("COmmone elements :",i);
