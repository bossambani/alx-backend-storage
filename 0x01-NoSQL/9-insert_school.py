#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection
    """
    doc = mongo_collection.insert_one(kwargs)

    return doc.inserted_id
