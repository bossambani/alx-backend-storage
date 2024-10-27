#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


def nginx_stats():
    """
    Python script that provides some stats about
    Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    # Count total logs
    total_logs = collection.count_documents({})

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Count GET requests with path=/status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Display stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_count} status check")


if __name__ == "__main__":
    nginx_stats()
