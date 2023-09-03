from functions import get_student_by_pk, check_fitness, get_profession_by_title, load_students, load_professions

number = int(input("Введите номер студента   \n"))
dict = []
job_dict = []
for stud in load_students():
    dict.append(stud["pk"])

if number in dict:
    stedent = get_student_by_pk(number)
else:
    print("У нас нет такого студента")
    quit()

print(f"Студент {stedent['full_name']}\nЗнает {','.join(stedent['skills'])}")

job_input = input(f"Выберите специальность для оценки студента {stedent['full_name']}    \n ")
for stud in load_professions():
    job_dict.append(stud["title"])

if job_input in job_dict:
    job = check_fitness(stedent, get_profession_by_title(job_input))
else:
    print("У нас нет такой специальности")
    quit()

print(f"Пригодность {job['fit_percent']} \n{stedent['full_name']} знает {job['has']} \n{stedent['full_name']} не знает {job['lacks']}")