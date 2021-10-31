number=float(input())
input_unit_of_measure=input()
output_unit_of_measure=input()
result = 0
if input_unit_of_measure == "m":
    if output_unit_of_measure == "cm":
        result = f"{number * 100:.3f}"
    else:
        result = f"{number * 1000:.3f}"
elif input_unit_of_measure == "cm":
    if output_unit_of_measure == "m":
        result = f"{number / 100:.3f}"
    else:
        result = f"{number * 10:.3f}"
else:
    if output_unit_of_measure == "cm":
        result = f"{number / 10:.3f}"
    else:
        result = f"{number / 1000:.3f}"
print(result)



