a=5
b=0
try:
    print("resource open")
    print(a/b)
    k=int(input("enter a no"))
    print(k)
except ZeroDivisionError as e: #if divided by zero
    print("no. cannot be divided by zero",e)
except ValueError as e:     #invalid input
    print("invalid input")
except Exception as e:
    print("something went wrong")
finally:
    print("resource closed")