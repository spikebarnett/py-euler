#!/usr/bin/python3
numbers=100
sumOfSqr=0
sqrOfSum=(1+numbers)*(numbers/2)
sqrOfSum*=sqrOfSum
for i in range(1,101):
	sumOfSqr+=i*i
print(sqrOfSum-sumOfSqr)

# 25164150