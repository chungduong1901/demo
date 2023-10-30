import math
a=int(input("Nhập cạnh tam giác thứ nhất:"));
b=int(input("Nhập cạnh tam giác thứ hai:"));
c=int(input("Nhập cạnh tam giác thứ ba:"));
cp=a+b+c
p=cp/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Chu vi = ", cp)
print("Diện tích = ", s)