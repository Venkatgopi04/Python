import time
A1=input("Enter your input:")
print()
a=A1[0:]
b=A1[::-1]
if a==b and b==a:
    print("Palindrome")
else:
    print("NOT  Palindrome")
print()
time.sleep(2)
print("End of an Application")