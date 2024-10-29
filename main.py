# Ethan Lawrence
# oct 28, 2024
# Lists mastery Check

# Input
john_info = []
grades_john = []
smith_info = []
grades_smith = []
# John
john_info.append('PARKER')
john_info.append('John')
john_info.append('Grand Traverce Academy')
john_info.append('Biology')

grades_john.append(90)
grades_john.append(95)
grades_john.append(20)
grades_john.append(82)
# Smith
smith_info.append('EDWARD')
smith_info.append('Smith')
smith_info.append('Grand Traverce Academy')
smith_info.append('Biology')

grades_smith.append(75)
grades_smith.append(80)
grades_smith.append(88)
grades_smith.append(82)

# Process
john_average = sum(grades_john) / len(grades_john)
smith_average = sum(grades_smith) / len(grades_smith)

# Output
print('Semester 1 Grade Report')
print('-------------')
# John
print(f'Student: {john_info[0]}, {john_info[1]}')
print(f'School: {john_info[2]}')
print(f'Course: {john_info[3]}')
print(f'Average Score: {john_average:,.2f} \n')
# Smith
print(f'Student: {smith_info[0]}, {smith_info[1]}')
print(f'School: {smith_info[2]}')
print(f'Course: {smith_info[3]}')
print(f'Average Score: {smith_average:,.2f} \n')