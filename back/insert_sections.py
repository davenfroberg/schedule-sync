import json
import connect

"""
This file contains the functions to generate insert queries for the Sections table in the database. This was used
to populate the Courses table with data from the JSON files in the data folder, sourced from various UBC related
websites.
"""


def generate_insert_queries(section_data):
    insert_queries = []

    for section in section_data:
        dept = section.get('dept')
        course_num = section.get('course_num')
        section_num = section.get('section_num')
        term = section.get('term')
        days = section.get('days')
        start_time, end_time = section.get('time').split('-')

        term_value = f"2023W{term}"

        sql_query = f"INSERT INTO Sections (term, section, daysOfWeek, startTime, endTime, courseNum, courseDept) " \
                    f"VALUES ('{term_value}', '{section_num}', '{days}', '{start_time}', '{end_time}', '{course_num}', '{dept}')"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    json_file_path = '../data/ubc_courses_data/all_section_list.json'

    json_data = read_json_file(json_file_path)

    insert_queries = generate_insert_queries(json_data)

    for query in insert_queries:
        try:
            connect.query(query)
        except Exception as e:
            print(e)
            print(query)