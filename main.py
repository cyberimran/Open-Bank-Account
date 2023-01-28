import time 
import random

ac=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
ac_number=""
try:
    name=input("Full Name: ")
    age=int(input("Age: "))
    number=int(input("Mobile Number: "))
    adress=input("Adress: ")
    upi=""
except Exception:
    print("Wrong Details!")
if len(str(age))<3 and len(str(age))>1:
    if len(str(number))==10:
        for i in range(0,12):
            ac_number=ac_number+str(random.choice(ac))
        upi=str(number)+"@imrancoding"
print("Please wait your account is being created")
time.sleep(3)
print("\n\n\n\nAccount details:\n")
print("Name:",name.title())
print("Bank Name: IMRAN CODING")
print(f"Account Number: {ac_number}")
print(f"Mobile Number: {number}")
print(f"Upi Id: {upi}")