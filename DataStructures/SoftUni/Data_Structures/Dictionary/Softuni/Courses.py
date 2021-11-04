# text = input()
#
# courses = {}
#
# while not text == 'end':
#     course, name = text.split(" : ")
#     if course not in courses:
#         courses[course] = []
#
#     courses[course].append(name)
#     text = input()
#
# sorted_list = dict(sorted(courses.items(), key=lambda kvp: -len(kvp[1])))
# for k, v in sorted_list.items():
#     print(f'{k}: {len(v)}')
# for v in sorted_list.values():
#     print(f'--{v}')
# [print(f'{k}: {len(v)}\n --{v}\n') for k, v in courses.items()]
# dict_order = sorted(courses.items(), key=lambda x: len(x[1], x[0]))

# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end
courses_info = {}

command = input()
while not command == 'end':
    cmd_info = command.split(" : ")
    course_name = cmd_info[0]
    student_name = cmd_info[1]

    if course_name not in courses_info:
        courses_info[course_name] = []
    if student_name not in courses_info[course_name]:
        courses_info[course_name].append(student_name)

    command = input()

for (course, students) in sorted(courses_info.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    print(f"{course}: {len(students)}")

    for student in sorted(students):
        print(f"-- {student}")