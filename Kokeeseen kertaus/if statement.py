times = 0

while times < 5:
    name = input("Write your name here: ")
    if len(name) < 3 and times <= 5:
        print("Name must be atleast 3 characters long. ")
        times += 1
    elif len(name) > 15 and times <= 5:
        print("Name must be less than 15 characters long. ")
        times += 1
    else:
        print(f"Hello {name}!")
        break

print("You have tried too many times!")

