
print(20*"=")
print("Simple Calculator")
print(20*"=" + "\n")

primary_number = float(input("Input first number = "))
operator = input("(+,-,x,/) : ")
secondary_number = float(input("Input second number = "))

if operator == "+":
     con = primary_number + secondary_number
     print(f"hasilnya adalah {con}")

elif operator == "-":
     con = primary_number - secondary_number
     print(f"hasilnya adalah {con}")

elif operator == "x" or operator == "*":
     con = primary_number * secondary_number
     print(f"hasilnya adalah {con}")

elif operator == "/":
     con = primary_number / secondary_number
     print(f"hasilnya adalah {con}")

else:
     print("command not found!, apk has been stoped")
