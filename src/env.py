from datetime import datetime
TİME_STAMP_PATTERN = "%m/%d/%Y, %H:%M:%S"

def is_more_than_one_hour(time: str):
    datetime_obj = datetime.strptime(time, TİME_STAMP_PATTERN)
    now = datetime.now()
    
    calculated_time = now - datetime_obj
    return bool(calculated_time.seconds // 3600)
