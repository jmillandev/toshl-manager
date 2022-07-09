from datetime import datetime
from config import SEPARATOR
import pytz

local = pytz.timezone("America/Caracas")

def has_containt_all_tags(tag_filters, data):
    tag_filters = set(tag_filters.split(SEPARATOR))
    return filter(
        lambda entry: len(tag_filters - set(entry['tags'])) == 0,
        data
    )


def utc_date(string_date):
    date_time = datetime.strptime(string_date, '%d/%m/%y')
    local_dt = local.localize(date_time, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

def optional_params(Endpoint, kwargs):
    return { key:kwargs.get(key) for key in Endpoint.OPTIONAL_PARAMS if kwargs.get(key) != None }
