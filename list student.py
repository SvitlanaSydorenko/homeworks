# 4. 
# Створити словник оцінок передбачуваних студентів 
# (Ключ – ПІ студента, значення – список оцінок студентів). 
# Знайти найуспішнішого і самого слабенького за середнім балом.


students = {
    '1.Sydorenko.Svitlana': [5,9,3,7,4,9,11,2],
    '2.Petrov.Ivan': [5,9,1,7,4,9,11,2],
    '3.Makarenko.Elena': [5,9,3,7,4,9,11,4],
    '4.Shevchuk.Oleg': [5,9,3,7,4,9,11,12],
    '5.Tkach.Maria': [5,9,3,7,4,4,11,7],
    '6.Ivanova.Natalia': [5,9,3,7,4,9,11,12],
    '7.Omelchenko.Viktoria': [5,9,3,7,4,9,11,12],
    '8.Martinuk.Liza': [5,9,3,7,4,9,11,6],
    '9.Chuchman.Olexander': [5,9,3,7,4,9,11,12],
    '10.Urchenko.Maksim': [5,9,3,7,4,9,11,12],
    '11.Kovalenko.Olga': [1,2,4,7,4,9,11,3],
}

def average(marks):
    sum = 0
    for mark in marks:
        sum = sum + mark
    return sum / len(marks)

hard = 0
low = 12
hard_student = ''
low_student = ''


for student, marks in students.items():
    if average(marks) > hard:
        hard = average(marks)
        hard_student = student

    if average(marks) < low:
        low = average(marks)
        low_student = student

print('Найуспішніший: ', hard_student)
print('Найслабший: ', low_student)
