#!/usr/bin/env python3

"""
Function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    if mongo_collection is None:
        return None
    schools = mongo_collection.find({"topics": topic})
    return schools
