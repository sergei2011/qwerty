import os
import json



'выгружаем список студентов'
def load_students():
    with open(os.path.join("..", "data", "students.json")) as f:
    #with open("..\data\students.json") as f:
       list_of_stud = json.load(f)

    return list_of_stud



'выгружаем список профессий'
def load_professions():
    with open(os.path.join("..", "data", "professions.json")) as f:
    #with open("..\data\professions.json") as f:
        list_of_job = json.load(f)

    return list_of_job


'находим студента и возращаем по номеру'
def get_student_by_pk(pk):
    dict = []
    for stud in load_students():

        if stud["pk"] == pk:
            return stud

'находим специальность по названию'
def get_profession_by_title(title):
    for prof in load_professions():
        if prof["title"] == title:
            return prof

'выводим специальности которые знает студент и которые ему надо подучить для профессии'
def check_fitness(student, profession):
    know = set(student["skills"]).intersection(set(profession["skills"]))
    not_know = set(student["skills"]).difference(set(profession["skills"]))
    ability_stud = {"has": know , "lacks": not_know, "fit_percent": round(len(know)/(len(know)+len(not_know))*100)}

    return ability_stud

