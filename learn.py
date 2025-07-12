try:
    print(10 + "2")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print("Continue...")
