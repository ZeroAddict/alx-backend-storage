#!/usr/bin/env python3
"""Module for task 11 filters by topic
"""


def schools_by_topic(mongo_collection, topic):
    """Function returns the list of school offering a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): collection to analyze
        topic (str): topic looked up to return filter.

    Returns:
        list: school having a specific topic.
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [sch for sch in mongo_collection.find(topic_filter)]
