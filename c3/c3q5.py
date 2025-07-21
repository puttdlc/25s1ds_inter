class stack:
    def __init__(self, values=[]):
        self.stack = values
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def get_stack(self):
        return self.stack

print("******** Parking Lot ********")
inp = input("Enter max of car / car in soi / operation : ")

max_car, car_in, instruction = inp.split(" / ")
command, value = instruction.split()
max_car, value = int(max_car), int(value)

cars = stack()

for car in car_in.split(","):
    cars.push(int(car))

if command == "arrive":
    if value in cars.get_stack():
        print(f"car {value} already in soi")
    else:
        if len(cars.get_stack()) + 1 <= max_car:
            print(f"car {value} arrive! : Add Car {value}")
            cars.push(value)
        else:
            print(f"car {value} cannot arrive : Soi Full")
elif command == "depart":
    if value in cars.get_stack():
        cars.stack.remove(value)
        print(f"car {value} depart ! : Car {value} was remove")
    else:
        print(f"car {value} cannot depart : Dont Have Car {value}")


print(cars.get_stack())

