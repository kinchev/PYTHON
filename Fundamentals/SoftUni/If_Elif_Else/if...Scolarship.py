income_in_leva = float(input())
average_success = float(input())
minimal_work_salary = float(input())
scholarship_social = int(minimal_work_salary * 0.35)
scholarship_excellent = int(average_success * 25)

if average_success >= 5.50:
    if income_in_leva > minimal_work_salary:
        print(f'You get a scholarship for excellent results {scholarship_excellent} BGN')
    else:
        if scholarship_excellent >= scholarship_social:
            print(f'You get a scholarship for excellent results {scholarship_excellent} BGN')

        else:
            print(f'You get a Social scholarship {scholarship_social} BGN')
elif average_success > 4.50:
    if income_in_leva < minimal_work_salary:
        print(f'You get a Social scholarship {scholarship_social} BGN')
    else:
        print(f'You cannot get a scholarship!')
else:
    print(f'You cannot get a scholarship!')
