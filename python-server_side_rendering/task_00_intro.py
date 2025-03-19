#!/usr/bin/python3
"""
Module for task_00_intro
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendee list.

    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    if not isinstance(template, str):
        print("Error: template must be a string")
        return []

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return []

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: all attendees must be dictionaries")
        return []

    if not template:
        print("Template is empty, no output files generated.")
        return []

    if not attendees:
        print("No data provided, no output files generated.")
        return []

    generated_files = []
    for i, attendee in enumerate(attendees, start=1):
        filled_template = template
        for placeholder in ["name", "event_title",
                            "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            filled_template = filled_template.replace(
                f"{{{placeholder}}}", value)

        file_name = f"output_{i}.txt"
        with open(file_name, "w") as f:
            f.write(filled_template)
        generated_files.append(file_name)

    return generated_files
