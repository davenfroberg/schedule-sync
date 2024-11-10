import json
import connect

"""
This file contains the functions to generate insert queries for the Requirements table in the database. This was used
to populate the Courses table with data from the JSON files in the data folder, sourced from various UBC related
websites.
"""

def generate_insert_queries(requirements_data):
    insert_queries = []

    for requirement in requirements_data:
        course_num = requirement.get('course_num')
        dept = requirement.get('dept')
        faculty = requirement.get('faculty')
        degreeName = requirement.get('name')

        sql_query = f"INSERT INTO Requirements (courseNum, courseDept, faculty, degreeName) VALUES ('{course_num}', '{dept}', '{faculty}', '{degreeName}')"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    json_file_path = '../data/requirement_data/requirement_list.json'

    json_data = read_json_file(json_file_path)

    insert_queries = generate_insert_queries(json_data)

    for query in insert_queries:
        try:
            connect.query(query)
        except:
            pass
