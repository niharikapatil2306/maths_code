import sympy as sy

def InvalidInputError(Exception):
    pass

def get_ip_type():
    while True: 
        try:
            ip_type = input("Enter \n 1 - For Scalar \n 2- For Vector \n 3 - For Matrix \n")
            if ip_type not in ['1', '2', '3']:
                raise InvalidInputError("Invalid input. \nPlease enter 1, 2, or 3.")
            return ip_type
        except InvalidInputError as e:
            print(f"Error: {e}")
            print("Invalid input. \nPlease enter 1, 2, or 3.")

def get_ip_val(t):
    if t == 1:
        ip_val = input("Enter the scalar value: ")
        return float(ip_val)
    
    elif t == 2:
        ip_val = input()

def input_values():

    ip_var = input("Enter variable name for value\n")

    ip_var = sy.Symbol(ip_var)

    ip_type = get_ip_type()



    print(ip_type)
    ip_val = input(f'Enter value for varibale {ip_var.name}\n')

    print(f"{ip_var}= {ip_val}")


input_values()


