def is_year_leap(year):
		if year%4 == 0:
			if year%400 == 0:
				print("Год:", year, 'True')
			elif year%100 != 0:
				print("Год:", year,'True')
			else:
				print("Год:", year,'False')
		else:
			print("Год:", year,'False') 			
year = int(input("Введите год: "))
is_year_leap(year)