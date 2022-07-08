from config import SEPARATOR

def has_containt_all_tags(tag_filters, data):
    tag_filters = set(tag_filters.split(SEPARATOR))
    return filter(
        lambda entry: len(tag_filters - set(entry['tags'])) == 0,
        data
    )
