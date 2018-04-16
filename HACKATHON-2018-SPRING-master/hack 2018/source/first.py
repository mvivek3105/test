#UMKC library containing books of itmes with prices#
umkc={"Python programming":60,"Web development":50,"C programming":40,"Java programming":30}
for index in umkc.items():
# To print all the books in the library#
 print(index)
#For minimum value
a=int(input("Enter the minimum value of the range:"))
#For maximum value
b=int(input("Enter the maximum value of the range:"))
x=dict((l,m) for l, m in umkc.items() if m>= a and m<=b)
print("you can get the books",x.keys())