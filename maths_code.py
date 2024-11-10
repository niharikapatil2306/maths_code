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
    if t == "1":
        ip_val = input("Enter the scalar value: \n")
        return float(ip_val)
    
    elif t == "2":
        ip_val = input("Enter the vector values (use comma's to separate values): \n")
        ip_val = [float(x) for x in ip_val.split(',') ]
        return sy.Matrix([ip_val])
    
    elif t == '3':
        rows = int(input("Enter number of rows for matrix \n"))
        cols = int(input("Enter number of columns for matrix \n"))
        ip_val=[]

        for row in range(rows):
            r = input(f"Enter {cols} values for row {row+1} (use comma's to separate values): \n ")
            r = [float(x) for x in r.split(',') ]
            if len(r) != cols:
                raise InvalidInputError(f"Row {row + 1} must have {cols} values. Please try again.")
            ip_val.append(r)

        return sy.Matrix(ip_val)

def input_values():

    ip_var = input("Enter variable name for value\n")

    ip_var = sy.Symbol(ip_var)

    ip_type = get_ip_type()

    ip_val = get_ip_val(ip_type)

    print(f"{ip_var}= {ip_val}")

def math_funcs(ip):
    return 1

input_values()


