#!/usr/bin/env python3

"""
This script is used for course notes.

Author: Erick Marin
Date: 11/28/2020
"""

import csv


def read_employees(csv_file_location):
    """
    Convert csv file to dictionary.

    Receives a CSV file as a parameter and returns a list of dictionaries from
    that file.
    """
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(
        open(csv_file_location), dialect="empDialect")
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


def process_data(employee_list):
    """
    Process employee data.

    Receive the list, employee_list, as a parameter and return a dictionary of
    department:amount.
    """
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    # set() method converts iterable elements to distinct elements
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)
    return department_data


def write_report(dictionary, report_file):
    """
    Generate report.

    Receives dictionary as a parameter and defines an output file to generate
    report.
    """
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+":"+str(dictionary[k])+"\n")
        f.close()


employee_list = read_employees(
    "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/Module_Review/data/employees.csv")
# print (employee_list)

dictionary = process_data(employee_list)
# print(dictionary)

write_report(
    dictionary, "/home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_2/Module_Review/data/report.txt")
