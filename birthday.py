from datetime import date , datetime


def birthday(month, day, year=2019):
	today = date.today()
	my_birthday = date(today.year, month, day)
	bday = date(year, month, day)
	if my_birthday > today or my_birthday < today:
		my_birthday = my_birthday.replace(year=today.year + 1 )
		time_to_birthday = my_birthday - today
		if  time_to_birthday.days > 0:
			print(str(time_to_birthday) + ' days to my ' + str(my_birthday.year) + '\'s ' + 'birthday')
			print("Your birthday will be on: " + datetime.strftime((today + time_to_birthday), "%y %b %a"))

		else:
			print(str(time_to_birthday) + ' days to my ' + str(my_birthday.year) + '\'s ' + 'birthday')
			print("Your birth will be on: " + datetime.strftime((today + time_to_birthday), "%y %b %a"))	


	if bday.year == today.year:
		bd = (bday - today)
		if bd.days > 0:
			print("my " + str(today.year) + '\'s ' + 'birthday has ' + str(bd.days) + ' days to go')
			print("Your birthday will be on: " + datetime.strftime((today + bd), "%y %b %a"))
		else:
			print(str(time_to_birthday) + ' days to my ' + str(my_birthday.year) + '\'s ' + 'birthday')
			print("Your birthday will be on: " + datetime.strftime((today + time_to_birthday), "%y %b %a"))	
birthday(4, 8)			



'''from datetime import datetime
now = datetime.now()
print(now)'''

