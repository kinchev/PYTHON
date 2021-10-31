judge=int(input())
final_grade=0
number_of_presentation=0
command=input()
while command!='Finish':
    current_presentation_name=command
    number_of_presentation += 1
    current_presentation_grade=0
    for presentation_grade in range(judge):
        grade=float(input())
        current_presentation_grade+=grade
    presentation_average_grade=current_presentation_grade/judge
    final_grade+=presentation_average_grade
    print(f'{current_presentation_name} - {presentation_average_grade:.2f}.')
    command=input()
final_average_grade=final_grade/number_of_presentation
print(f"Student's final assessment is {final_average_grade:.2f}.")




