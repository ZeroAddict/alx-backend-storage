#!/usr/bin/env python3
"""Module for task 8
"""


def list_all(mongo_collection):
    """Function retrieves documents list in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): collection to be analyzed

    Returns:
        list:  all documents in a collection or empty list.
    """
    return [sch for sch in mongo_collection.find()]
