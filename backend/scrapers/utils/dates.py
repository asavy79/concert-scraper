from datetime import datetime


def format_sz_time(date_str: str):
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    formatted = dt.replace(hour=23, minute=59, second=59).strftime(
        '%Y-%m-%dT%H:%M:%SZ')
    return formatted
