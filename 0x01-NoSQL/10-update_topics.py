#!/usr/bin/env python3
"""Module for task 10 update_topics
"""


def update_topics(mongo_collection, name, topics):
    """Function changes all topics of a school document based on name arg.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze
        name (str): school name to be updated.
        topics (list): list of topics in the school.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
