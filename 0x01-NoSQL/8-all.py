#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    return the documents in the collection
    """
    doc = mongo_collection.find()

    if not doc:
        return []

    return doc
