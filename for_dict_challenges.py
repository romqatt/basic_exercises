from collections import Counter
import operator
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names_counter = Counter([student['first_name'] for student in students])
for name, count in names_counter.items():
	print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
	{'first_name': 'Петя'},
	{'first_name': 'Петя'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names_counter = Counter([student['first_name'] for student in students])
max_names = max(names_counter, key=names_counter.get)
print(f"Most popular name: {max_names} with count {names_counter[max_names]}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
		{'first_name': 'Оля'},
        {'first_name': 'Вася'},
		{'first_name': 'Петя'},
		{'first_name': 'Женя'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
		{'first_name': 'Вася'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
		{'first_name': 'Вася'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
class_counter = 1
for school_class in school_students:
	names_counter = Counter([student['first_name'] for student in school_class])
	max_names = max(names_counter, key=names_counter.get)
	class_counter += 1
	print(f'Most popular name in class {class_counter}: {max_names} with count {names_counter[max_names]}')



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Миша'}, {'first_name': 'Олег'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
	male_count = 0
	female_count = 0
	students_names = [student['first_name'] for student in school_class['students']]
	for name in students_names:
		if is_male[name]:
			male_count += 1
		else:
			female_count += 1
	print(f"Class {school_class['class']}: male {male_count}, female {female_count}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Миша'}, {'first_name': 'Даша'}]},
	{'class': '2b', 'students': [{'first_name': 'Маша'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
	{'class': '3a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Миша'}, {'first_name': 'Даша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
	'Даша': False,
}

def gender_count(school_class, is_male):
	male_count = 0
	female_count = 0
	students_names = [student['first_name'] for student in school_class['students']]
	for name in students_names:
		if is_male[name]:
			male_count += 1
		else:
			female_count += 1
	school_class['male_count'] = male_count
	school_class['female_count'] = female_count
	return(school_class)

school = [gender_count(school_class, is_male) for school_class in school]

max_male = 0
max_female = 0
for school_class in school:
	if school_class['male_count'] > max_male:
		max_male = school_class['male_count']
		max_male_class = school_class
	if school_class['female_count'] > max_female:
		max_female = school_class['female_count']
		max_female_class = school_class
		
print(f"Max male students in class {max_male_class['class']}")
print(f"Max female students in class {max_female_class['class']}")