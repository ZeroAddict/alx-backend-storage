#!/usr/bin/env python3
"""Module for task 12nginx_ log_stats
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """script gives some about Nginx logs stored in MongoDB.

    Args:
        nginx_collection (pymongo.collection.Collection): collection to analyze
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    mthds = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in mthds:
        req_count = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_chcks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_chcks_count))


def run():
    """Gives Nginx logs stats stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
