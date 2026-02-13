marks = [45, 78, 90, 33, 60]

pass_students_count = 0
fail_students_count = 0

for mark in marks:
    if mark >= 50:
        pass_students_count += 1
    else:
        fail_students_count += 1

print("Total Students:", len(marks))
print("Number of Pass Students:", pass_students_count)
print("Number of Fail Students:", fail_students_count)