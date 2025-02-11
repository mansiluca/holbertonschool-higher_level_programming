#!/usr/bin/python3
"""
Module for task_02_csv
"""


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file
    """

    import csv
    import json
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
