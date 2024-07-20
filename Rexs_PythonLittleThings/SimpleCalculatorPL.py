result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        if wait_for_number:
            input_value = input("Podaj liczbę: ")
            operand = float(input_value)
            wait_for_number = False
        else:
            input_value = input("Podaj operator (+, -, *, /): ")
            if input_value not in ['+', '-', '*', '/']:
                raise ValueError(
                    f"{input_value} nie jest '+' lub '-' lub '/' lub '*'")
            if operator == input_value:
                raise ValueError(
                    "Błąd! Wprowadzono operator dwa razy z rzędu!")
            operator = input_value
            wait_for_number = True

        if operand is not None and operator is not None:
            if operator == '+':
                result = result + operand if result is not None else operand
            elif operator == '-':
                result = result - operand if result is not None else -operand
            elif operator == '*':
                result = result * operand if result is not None else 0
            elif operator == '/':
                if operand == 0:
                    raise ZeroDivisionError("Nie można dzielić przez zero!")
                result = result / operand if result is not None else 0

            operand = None
            operator = None

    except ValueError as ve:
        print(f"Błąd: {ve}")
    except ZeroDivisionError as zde:
        print(f"Błąd: {zde}")

    if input_value == '=':
        if result is not None:
            print(f"Wynik: {result}")
        else:
            print("Nie podano żadnych operacji.")
        break

"""
Another Version of it 

def perform_operation(operator, operand, result):
    if operator == '+':
        return result + operand
    elif operator == '-':
        return result - operand
    elif operator == '*':
        return result * operand
    elif operator == '/':
        return result / operand


result = None
operand = None
operator = None
wait_for_number = True
operators = ['+', '-', '*', '/']

while True:
    user_input = input()

    if user_input == '=':
        if result is None:
            print("Brak wyniku do wyświetlenia.")
        else:
            print(f"Wynik: {result}")
        break

    if wait_for_number is True:
        try:
            operand = float(user_input)
        except ValueError:
            print(f"'{user_input}' nie jest liczbą. Spróbuj ponownie")
            continue

        if operator is not None:
            result = perform_operation(operator, operand, result)
            operator = None
        else:
            result = operand

        wait_for_number = False

    else:
        if user_input not in operators:
            print(f"'{user_input}' nie jest '+' lub '-' lub '/' lub '*'. Spróbuj ponownie")
            continue

        operator = user_input
        wait_for_number = True
"""
"""
num = 0 
operation = None 
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]
while True:
    if reset is True:
        num = int(input("Podaj liczbę startową:") ) 
        reset = False
    operation = input("Podaj operację arytmetyczną jak np." + str(calcOperations) + " lub exit jeśli koniec lub reset: "
    if operation == "exit": break if operation == "reset":
        reset = True
        continue
    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja.")
        continue
        
    secondNum = int(input("Podaj drugą liczbę:"))
    if operation == "+":
        result = num + secondNum
    if operation ==
        result = num - secondNum
    if operation
        result = num secondNum
    if operation == "/";
        result = num / secondNum
    if operation == "**";
        result = num ** secondNum
        
    print("Wynik operacji" + str(num) + " " operation + str(secondNum) + " " =  str(result))
    num = result 
    result = None
"""