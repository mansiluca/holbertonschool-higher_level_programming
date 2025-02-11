#!/usr/bin/python3
"""
Module for task_03_xml
"""


def serialize_to_xml(data, filename):
    """
    serializes an object to a text file, using an XML representation
    """
    import xml.etree.ElementTree as ET
    root = ET.Element("data")
    for key, value in data.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    deserializes an XML representation from a text file
    """
    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
