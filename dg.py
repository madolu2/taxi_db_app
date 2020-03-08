import random as r


class DriverGenerator:
	def generate_name(self):
		first_name = ['Август', 'Гавриил', 'Динор', 'Александр', 'Богдан', 'Валентин', 'Дорот', 'Мирослав']
		patronymic = ['Александров', 'Дмитриев', 'Федоров', 'Оскаров', 'Ильич', 'Олегов']
		last_name = ['Аверинцев', 'Абаимов', 'Кабанов', 'Голубев', 'Петров', 'Райкин', 'Савояров', 'Студентов']

		#True - male // False - female
		sex = r.choice([True, False])
		name = {}
		if sex:
			name['sex'] = 'Male'
		else:
			name['sex'] = 'Female'
		suffix = ''
		psuffix = 'ич'

		if not sex:
			suffix = 'а'
			psuffix = 'на'
		name['lname'] = f'{r.choice(last_name)}{suffix}'
		name['fname'] = f'{r.choice(first_name)}{suffix}'
		name['pname'] = f'{r.choice(patronymic)}{psuffix}'

		return name

	def generate_date(self):

		year = r.choice(['2017', '2018', '2019'])
		month = ''
		day = ''
		
		month += str(r.randint(0, 1))

		if int(month) == 1:
			month += str(r.randint(0, 2))
		else:
			month += str(r.randint(1, 9))

		if int(month) == 2:
			day += str(r.randint(1,29))
		else:
			day += str(r.randint(1,31))
		
		if len(day) < 2:
			day = f'0{day}'

		return f'{year}-{month}-{day}'

	def generate_area(self):
		def generate_street():
			streets = ['Красноармейский', 'Ленина', 'Германа-Титова', 'Лихачева', 'Петра-Сухова',
			'Эмилии-Алексеевой', 'Комсомольский', 'Брестская', 'Васильковая улица',
			'Гаражная улица', 'Жемчужная улица', 'Магистральный проезд', 'Обская улица', 'Урожайная улица', 'Чапаева']
			return r.choice(streets)

		def generate_home_num():
			return r.randint(1,100)

		return f'{generate_street()}', f'д{generate_home_num()}'

	def generate_driver(self):
		data = self.generate_name()
		driver = {
		"name": data['fname'],
		"lname": data['lname'],
		"experience": r.randint(5,15),
		"fine": r.choice([0, 1]),
		"commendation": r.choice([0, 1])
	}
		return driver

	def generate_call(self):
		length = r.randint(3,50)
		call_area, ca_home = self.generate_area()
		destination_area, da_home = self.generate_area()
		call = {
		"date": self.generate_date(),
		"length": length,
		"call_area": call_area,
		"ca_home": ca_home,
		"destination_area": destination_area,
		"da_home": da_home,
		"price": (100 + length*15)
	}
		return call

	def generate_auto(self):
		colors = ['Blue', 'Gray', 'Black', 'White', 'Red', 'Green', 'Purple', 'Yellow']
		brands = ['Renault Logan', 'Toyota Corolla', 'Lada Priora', 'Daewoo Nexia',
		'Lada 2110', 'Lada Granta', 'Kia Rio', 'Mitsubishi Lancer',
		'Toyota Camry','Hyundai Solaris', 'Chevrolet Lacetti']

		def generate_auto_number():
			literals = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
			number = ''
			number += r.choice(literals)
			for i in range(3):
				number+=str(r.randint(0,9))
			for i in range(2):
				number += r.choice(literals)
			number+= ' 22RUS'
			return number

		auto = {
		"color": r.choice(colors),
		"brand": r.choice(brands),
		"number": generate_auto_number()
		}
		return auto





