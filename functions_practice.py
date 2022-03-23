def hello():
    print("Hey user! Great to see you!")
hello()

def pack(first, second, third):
    print([first, second, third])
pack("camera", "soap", "sunscreen")

def eat_lunch(list):
    if len(list) > 1:
        print(f"First, I eat {list}")
        for i in list[1:]:
            print(f"then, I eat {i}")
    elif len(list) == 1:
        print(f"I eat {list[0]}")
    else: print("I actually don't eat lunch")

food = ["soup", "tacos", "pasta", "salad", "burgers", "candy"]
single = ["nachos"]
nothing = []
eat_lunch(single)


