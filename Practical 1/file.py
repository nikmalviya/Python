import calendar as cal
import datetime
print('Enter Your Details')
name = input('Enter Your Name :')
birth_date = input('Enter Your BirthDate :')
sem = input('Enter Semester :')
print("Data Submitted On : "+datetime.datetime.now().isoformat())
print('Name : '+name)
print('Birth Date : '+birth_date)
print('Semester : '+sem)
age = datetime.date.today().year - int(birth_date[:4])
print('Age :'+str(age))



