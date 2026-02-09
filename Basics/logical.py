#logical operator
a=True
b=False

print("a=",a," b=",b)
print("a and b:", a and b) #false
print("a or b:", a or b)   #true
print("not a:", not a)     #false
print("not b:", not b)     #true

#practical example
age = 20
has_license = True

can_drive = age >= 18 and has_license
print("Can drive?", can_drive) #true
