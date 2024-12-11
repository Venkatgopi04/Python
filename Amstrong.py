num=int(input()) 
length=len(str(num))
tem=num 
sum=0 
stnum=str(num)
for i in stnum:
    digit=tem%10
    sum+=digit**length 
    tem=tem//10 
if sum==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")