import re


def validate_query(query):

    if len(query) > 300:
        raise ValueError("Query too long")

    if re.search(r"(ignore previous instructions)", query, re.IGNORECASE):
        raise ValueError("Potential prompt injection detected")

    return query