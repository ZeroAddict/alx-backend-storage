#!/usr/bin/env python3
"""Module for task 9
"""


def insert_school(mongo_collection, **kwargs):
    """Function inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze

    Returns:
        str: retrns the new id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
