hours_of_exam = int(input())
minutes_of_exam = int(input())
hours_of_arrived = int(input())
minutes_of_arrived = int(input())
time_of_exam = hours_of_exam * 60 + minutes_of_exam
time_of_arraved = hours_of_arrived * 60 + minutes_of_arrived
if time_of_arraved > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arraved <= time_of_exam:
    print('On time')
else:
    print('Early')
if time_of_exam-60<time_of_arraved<time_of_exam:
    print(f'{time_of_exam-time_of_arraved} minutes before the start')
elif time_of_arraved<=time_of_exam-60:
    diffrence=time_of_exam-time_of_arraved
    hours=diffrence//60
    minutes=diffrence%60
    print(f'{hours}:{minutes:0>2d} hours before the start')
elif time_of_exam<time_of_arraved<time_of_exam+60:
    print(f'{time_of_arraved-time_of_exam} minutes after the start')
elif time_of_arraved>=time_of_exam+60:
    difference=time_of_arraved-time_of_exam
    hours=difference//60
    minutes=difference%60
    print(f'{hours}:{minutes:0>2d} hours after the start')