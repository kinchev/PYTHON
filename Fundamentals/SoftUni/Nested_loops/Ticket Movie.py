film_name=input()
student_counter=0
kid_counter=0
standard_counter=0
while film_name!='Finish':
    free_space = int(input())
    current_people_count=0
    for tickets in range(1,free_space+1):
        ticket_type=input()
        if ticket_type=='End':
            break
        elif ticket_type=='student':
            student_counter+=1
        elif ticket_type=='kid':
            kid_counter+=1
        elif ticket_type=='standard':
            standard_counter+=1
        current_people_count+=1
    percent=current_people_count/free_space*100
    print(f'{film_name}-{percent:.2f}% full')
    film_name=input()

total_ticket=kid_counter+standard_counter+student_counter
print(total_ticket)
student_procent=student_counter/total_ticket*100
print(f'{student_procent}')