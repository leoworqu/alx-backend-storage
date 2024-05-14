#!/usr/bin/env python3

"""
Function that inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    """
    if mongo_collection is None:
        return None
    inserted_document = mongo_collection.insert_one(kwargs)
    return inserted_document.inserted_id
