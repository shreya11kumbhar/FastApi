from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def show():
    return "Hey"

@app.post("/operations")
def operations(choice: int, num1: int, num2: int):
    if choice == 1:
        return f"Addition: {num1 + num2}"
    elif choice == 2:
        return f"Substraction: {num1 - num2}"
    elif choice == 3:
        return f"Multilpication: {num1*num2}"
    elif choice == 4:
        return f"Division: {num1//num2}"
    else:
        return "Error: Entered Wrong choice"

@app.post("/echo")
def showstring(string1: str):
    return f"Enter String is: {string1}"
