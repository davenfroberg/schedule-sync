import json
import connect

"""
This file contains the functions to generate insert queries for the Courses table in the database. This was used
to populate the Courses table with data from the JSON files in the data folder, sourced from various UBC related
websites.
"""

def generate_insert_queries(course_data):
    insert_queries = []

    for course in course_data:
        course_num = course.get('courseNum')
        dept = course.get('dept')

        sql_query = f"INSERT INTO Courses (courseNum, dept) VALUES ('{course_num}', '{dept}')"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    json_file_path = '../data/ubc_dept_data/CPSC.json'

    json_data = read_json_file(json_file_path)

    insert_queries = generate_insert_queries(json_data)

    for query in insert_queries:
        try:
            connect.query(query)
        except:
            pass
