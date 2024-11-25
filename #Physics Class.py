#Physics Class

def f_to_c(f_temp):
    temp_c = (f_temp - 32) * 5 / 9\
    
    return print(temp_c)



def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32

    return print(f_temp)


def f_to_c_or_c_to_f():
    while True:
        f_or_c = str(input("chosse c to f, press f, or f to c, press c: "))
        
        if f_or_c != "f" and f_or_c != "c":
            print("invalid comand")            

        elif f_or_c == "f":
            f = input("c temp: ")
            c_to_f(int(f))
            
            break

        elif f_or_c == "c":
            c = input("f temp: ")

            f_to_c(int(c))
            break


def get_force():
    inputs = input("give mass, acceleration")
    data = inputs.split(",")
    data = [item.strip() for item in data]
    force = int(data[0]) * int(data[1])
    return force, print(force)

def get_energy():
    mass = int(input("mass: "))
    c = (3*10**8)
    energy = (mass * (c * c))
    return print("%s energy" %energy)

def get_work():
    inputs = input("give mass, acceleration, distance")
    data = inputs.split(",")
    data = [item.strip() for item in data]
    work = int(data[0]) * int(data[1]) * int(data[2])
    return print("{x} joules over {y} meters".format(x=work, y=data[2]))


def chosse_function():
    while True:
        print("chosse, f_to_c_or_c_to_f, get_force, get_energy, get_work")
        print("exit, to exit")
        choice = input("your choice: ")

        if choice == "f_to_c_or_c_to_f":
            f_to_c_or_c_to_f()
            

        elif choice == "get_force":
            get_force()
            

        elif choice == "get_energy":
            get_energy()
            

        elif choice == "get_work":
            get_work()
        
        elif choice == "exit":
            break

        else: 
            print("invalid command")
            

chosse_function()