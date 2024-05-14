#!/usr/bin/env python3

"""
Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    pipeline = [
        {
            "$unwind": "$scores"
        },
        {
            "$group": {
                "_id": "$_id",
                "averageScore": {"$avg": "$scores.score"},
                "name": {"$first": "$name"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "averageScore": 1
            }
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
