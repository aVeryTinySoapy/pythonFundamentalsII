""" x = "message..."
print(x)
print("Hello World") """

# python if else statement
x = 10
y = 5

if x > y:
    print(x,"is greater than",y)
else:
    print(x,"is lesser than",y)

# python if... else if statement
x = 5
y = 5
x = 3
y = 3
x = 5
if x > y: # 5 > 3
    print(x,"is greater than",y)
elif y > x:
    print(x,"is lesser than",y)
else:
    print(x,"both number is equal")