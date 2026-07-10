import os

print("Database Location:", os.path.abspath("calculator.db"))

from database import conn, cursor

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero."

else:
    result = "Invalid operator!"

print("Result:", result)
cursor.execute(
    "INSERT INTO history (num1, operator, num2, result) VALUES (?, ?, ?, ?)",
    (num1, operator, num2, str(result))
)
cursor.execute("SELECT * FROM history")
rows = cursor.fetchall()

print(rows)
conn.commit()
conn.close()