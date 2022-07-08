from datetime import datetime

from config import SEPARATOR

def has_containt_all_tags(tag_filters, data):
    tag_filters = set(tag_filters.split(SEPARATOR))
    return filter(
        lambda entry: len(tag_filters - set(entry['tags'])) == 0,
        data
    )


def utc_date(string_date):
    date_time = datetime.strptime(string_date, '%d/%m/%y')
    return date_time.strftime('%Y-%m-%dT%H:%M:%SZ')
