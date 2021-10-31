failed_threshold = int(input())
failed_times = 0
solved_problem_count = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problem_count += 1
    last_problem = problem_name
if has_failed:
    print(f'You need a break, {failed_threshold} poor grades.')
    print(f'number of problems: {solved_problem_count}')
    print(f'last problem: {last_problem}')
