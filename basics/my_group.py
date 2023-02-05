groupmates = [
	{
		"name": "Михаил",
		"surname": "Ющенко",
		"exams": ["Философия", "История", "Русский язык и культура речи"],
		"marks": [3, 5, 5]
	},
	{
		"name": "Демид",
		"surname": "Смирнов",
		"exams": ["Философия", "История", "Русский язык и культура речи"],
		"marks": [4, 3, 5]
	},
	{
		"name": "Данил",
		"surname": "Сидорук",
		"exams": ["Философия", "История", "Русский язык и культура речи"],
		"marks": [5, 4, 4]
	},
	{
		"name": "Алан",
		"surname": "Шарифуллин",
		"exams": ["Философия", "История", "Русский язык и культура речи"],
		"marks": [4, 4, 5]
	},
	{
		"name": "Александр",
		"surname": "Плешаков",
		"exams": ["Философия", "История", "Русский язык и культура речи"],
		"marks": [4, 3, 5]
	}
]


def print_students(students, threshold):
	print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
	for student in filter(lambda e: sum(e["marks"]) / len(e["marks"]) > threshold, students):
		print(
			student["name"].ljust(15), student["surname"].ljust(10),
			str(student["exams"]).ljust(30), str(student["marks"]).ljust(20)
		)


def main():
	threshold = float(input("Введите средний балл, по которому будем проводиться фильтрация: "))
	print_students(groupmates, threshold)


if __name__ == "__main__":
	main()