import pandas as pd
import math
import requests
from tqdm import tqdm
import regex as re
import datetime as dt
import numpy as np

def treat_vacancy_name_group(df, group_number):
    tmp_list = []
    unique_min_salary = df[df["min_salary"].notna()]["min_salary"].unique()
    unique_max_salary = df[df["max_salary"].notna()]["max_salary"].unique()
    max_days = df["days_passed"].max()
    min_days = df["days_passed"].min()
    avg_days = df["days_passed"].mean()
    unique_experience_values = df["experience"].unique()
    unique_employment_values = df["employment"].unique()
    unique_schedule_values = df["schedule"].unique()
    for row in range(len(unique_min_salary)):
        tmp_list.append(0)
    min_salary_dict = dict(zip(unique_min_salary, tmp_list))
    tmp_list = []
    for row in range(len(unique_max_salary)):
        tmp_list.append(0)
    max_salary_dict = dict(zip(unique_max_salary, tmp_list))
    tmp_list = []
    for row in range(len(unique_vacancies_names)):
        tmp_list.append(0)
    vacancies_dict = dict(zip(unique_vacancies_names, tmp_list))
    tmp_list = []
    for row in unique_experience_values:
        tmp_list.append(0)
    experience_dict = dict(zip(unique_experience_values, tmp_list))
    tmp_list = []
    for row in unique_employment_values:
        tmp_list.append(0)
    employment_dict = dict(zip(unique_employment_values, tmp_list))
    tmp_list = []
    for row in unique_schedule_values:
        tmp_list.append(0)
    schedule_dict = dict(zip(unique_schedule_values, tmp_list))
    for index, Row in df.iterrows():
        if vacancies_dict.get(Row["name"]) is not None:
            vacancies_dict[Row["name"]] += 1
        if experience_dict.get(Row["experience"]) is not None:
            experience_dict[Row["experience"]] += 1
        if employment_dict.get(Row["employment"]) is not None:
            employment_dict[Row["employment"]] += 1
        if schedule_dict.get(Row["schedule"]) is not None:
            schedule_dict[Row["schedule"]] += 1
        if min_salary_dict.get(Row["min_salary"]) is not None:
            min_salary_dict[Row["min_salary"]] += 1
        if max_salary_dict.get(Row["max_salary"]) is not None:
            max_salary_dict[Row["max_salary"]] += 1
    f = open("VacancyNameGroups/salary_group" + str(group_number) + ".txt", "w", encoding="utf8")
    f.write(
        "Max = " + str(max_days) + "\n" + "Min = " + str(max_days) + "\n" + "Average = " + str(avg_days) + "\n" + "\n")
    for key in uniq_key_skills:
        f.write(str(key) + "\t" + str(uniq_key_skills[key]) + "\n")
    f.write("----------------" + "\n")
    for key in min_salary_dict:
        f.write(str(key) + "\t" + str(min_salary_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in max_salary_dict:
        f.write(str(key) + "\t" + str(max_salary_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in vacancies_dict:
        f.write(str(key) + "\t" + str(vacancies_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in experience_dict:
        f.write(str(key) + "\t" + str(experience_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in employment_dict:
        f.write(str(key) + "\t" + str(employment_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in schedule_dict:
        f.write(str(key) + "\t" + str(schedule_dict[key]) + "\n")
    f.write("----------------" + "\n")
    f.close()



def treat_max_salary_group(df, group_number):
    tmp_list = []
    unique_vacancies_names = df["name"].unique()
    unique_experience_values = df["experience"].unique()
    unique_employment_values = df["employment"].unique()
    unique_schedule_values = df["schedule"].unique()
    for row in range(len(unique_vacancies_names)):
        tmp_list.append(0)
    vacancies_dict = dict(zip(unique_vacancies_names,tmp_list))
    tmp_list = []
    for row in unique_experience_values:
        tmp_list.append(0)
    experience_dict = dict(zip(unique_experience_values, tmp_list))
    tmp_list = []
    for row in unique_employment_values:
        tmp_list.append(0)
    employment_dict = dict(zip(unique_employment_values, tmp_list))
    tmp_list = []
    for row in unique_schedule_values:
        tmp_list.append(0)
    schedule_dict = dict(zip(unique_schedule_values, tmp_list))
    tmp_list = []
    max_days = df["days_passed"].max()
    min_days = df["days_passed"].min()
    avg_days = df["days_passed"].mean()
    for index, Row in df.iterrows():
        if vacancies_dict.get(Row["name"]) is not None:
            vacancies_dict[Row["name"]] += 1
        if experience_dict.get(Row["experience"]) is not None:
            experience_dict[Row["experience"]] += 1
        if employment_dict.get(Row["employment"]) is not None:
            employment_dict[Row["employment"]] += 1
        if schedule_dict.get(Row["schedule"]) is not None:
            schedule_dict[Row["schedule"]] += 1
    f = open("SalaryGroups/salary_group" + str(group_number) + ".txt", "w", encoding="utf8")
    f.write("Max = " + str(max_days) + "\n" + "Min = " + str(max_days) + "\n" + "Average = " + str(avg_days) + "\n"+ "\n")
    for key in vacancies_dict:
        f.write(str(key) + "\t" + str(vacancies_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in experience_dict:
        f.write(str(key) + "\t" + str(experience_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in employment_dict:
        f.write(str(key) + "\t" + str(employment_dict[key]) + "\n")
    f.write("----------------" + "\n")
    for key in schedule_dict:
        f.write(str(key) + "\t" + str(schedule_dict[key]) + "\n")
    f.write("----------------" + "\n")
    f.close()


# url_vacancies = 'https://api.hh.ru/vacancies?'
# params = {'area': 113, 'specialization': 1.221, "per_page": 100}
# url_vacancy = 'https://api.hh.ru/vacancies/'
# request_vacancies = requests.get(url_vacancies, params).json()
# found = 2000
# pages = 20
# vacancies_dict = {
#     "name": [None] * found,
#     "area": [None] * found,
#     "min_salary": [None] * found,
#     "max_salary": [None] * found,
#     "employer": [None] * found,
#     "created_at": [None] * found,
#     "days_passed": [None] * found,
#     "experience": [None] * found,
#     "employment": [None] * found,
#     "schedule": [None] * found,
#     "description": [None] * found,
#     "responsibility": [None] * found,
#     "requirement": [None] * found,
#     "conditions": [None] * found,
#     "key_skills": [None] * found,
# }
# count = 0
#
# for i in tqdm(range(pages)):
#     params["page"] = i
#     vacancies = requests.get(url_vacancies, params).json()["items"]
#     for j in range(len(vacancies)):
#         vacancy = requests.get(url_vacancy + vacancies[j]["id"]).json()
#         vacancies_dict["name"][count] = vacancy["name"]
#         vacancies_dict["area"][count] = vacancy["area"]["name"]
#         if vacancy["salary"] is not None:
#             vacancies_dict["min_salary"][count] = vacancy["salary"]["from"]
#             vacancies_dict["max_salary"][count] = vacancy["salary"]["to"]
#         vacancies_dict["employer"][count] = vacancy["employer"]["name"]
#         vacancies_dict["created_at"][count] = vacancy["created_at"]
#         vacancies_dict["experience"][count] = vacancy["experience"]["name"]
#         vacancies_dict["employment"][count] = vacancy["employment"]["name"]
#         vacancies_dict["schedule"][count] = vacancy["schedule"]["name"]
#         vacancies_dict["description"][count] = vacancy["description"]
#         vacancies_dict["responsibility"][count] = vacancies[j]["snippet"]["responsibility"]
#         vacancies_dict["requirement"][count] = vacancies[j]["snippet"]["requirement"]
#         if len(vacancy["key_skills"]) > 0:
#             vacancies_dict["key_skills"][count] = vacancy["key_skills"][0]["name"]
#             for k in range(1, len(vacancy["key_skills"])):
#                 vacancies_dict["key_skills"][count] += ";" + vacancy["key_skills"][k]["name"]
#         count += 1
# df = pd.DataFrame(vacancies_dict)
# df['description'] = df['description'].apply(lambda x: (re.sub(r'<.*?>', '', str(x))))
# df['created_at'] = df['created_at'].apply(lambda x: (
#     re.sub(r'(?<date>\d{4}-\d{2}-\d{2}).*', re.match("(?<date>\d{4}-\d{2}-\d{2}).*", str(x))["date"], str(x))))
# df["created_at"] = pd.to_datetime(df["created_at"])
# df["days_passed"] = pd.Series([(dt.datetime.today() - c).days for c in df["created_at"]])
# df.to_csv('all.csv', sep=";", encoding="utf-8-sig")
df = pd.read_csv('all.csv', sep=";", encoding="utf-8-sig")
df = df.sort_values(['max_salary', 'min_salary'], ascending=[True, True])

min_salary = int(df["max_salary"].min())
max_salary = int(df["max_salary"].max())
step = (max_salary-min_salary) / 10
tmpDF = []
i = 0
group_number = 1
for index, row in df.iterrows():
    if i < 9:
        if row["max_salary"] < min_salary + step*(i+1):
            tmpDF.append(row)
        else:
            workingDF = pd.DataFrame(tmpDF)
            workingDF.to_csv("SalaryGroups/salary_group" + str(group_number) + ".csv", sep=";", encoding="utf-8-sig")
            treat_max_salary_group(workingDF, group_number)
            workingDF = []
            group_number += 1
            i += 1
    elif i == 9:
        if row["max_salary"] < max_salary:
            tmpDF.append(row)
        else:
            workingDF = pd.DataFrame(tmpDF)
            workingDF.to_csv("SalaryGroups/salary_group" + str(group_number) + ".csv", sep=";", encoding="utf-8-sig")
            treat_max_salary_group(workingDF, group_number)
            workingDF = []
            group_number += 1
            i += 1
print("Done salary information!")
group_c = 1
unique_vacancies_names = df["name"].unique()
uniq_key_skills = {}
key_skills = [c for c in df["key_skills"].str.split(";")]
again = True
for i in range(len(key_skills)):
    if not isinstance(key_skills[i],list):
        key_skills[i] = [df["name"][i]]
for j in range(len(key_skills)):
    if key_skills[j] is not None:
        if len(key_skills[j]) > 0:
            for k in range(len(key_skills[j])):
                if not key_skills[j][k] in uniq_key_skills:
                    uniq_key_skills[key_skills[j][k]] = 0 * len(df["name"].unique())
for i in range(len(unique_vacancies_names)):
    group = df[df["name"] == unique_vacancies_names[i]]
    group.to_csv("VacancyNameGroups/salary_group" + str(group_c) + ".csv", sep=";", encoding="utf-8-sig")
    treat_vacancy_name_group(group,group_c)
    print(str(i))
    group_c += 1
for key in uniq_key_skills:
    for j in range(len(key_skills)):
        for k in range(len(key_skills[j])):
            if key_skills[j][k] in uniq_key_skills:
                uniq_key_skills[key_skills[j][k]] += 1
                print(str(j)+ " "+str(k))
f = open("SalaryGroups/salary_group" + str(group_c-1) + ".txt", "a", encoding="utf8")
for key in uniq_key_skills:
    f.write(str(key) + "\t" + str(uniq_key_skills[key]) + "\n")
f.write("----------------" + "\n")
f.close()
print("Done vacancies information!")
