import re
from datetime import datetime, timedelta

def parse_log_timestamp(log_timestamp):
    return datetime.strptime(log_timestamp, '%b %d %H:%M:%S.%f')

def filter_recent_logs(log_lines, minutes=5):  
    log_pattern = re.compile(r'^\*(?P<month>\w{3})\s+(?P<day>\d{1,2})\s+(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})\.(?P<millisecond>\d{3}):')
    recent_logs = []
    now = datetime.now()
    time_threshold = now - timedelta(minutes=minutes)
    # debug_info = []
    # debug_info.append(f"Current time: {now}")
    # debug_info.append(f"Time threshold: {time_threshold}")
    # debug_info.append(f"Log patter: {log_pattern}")


    for line in log_lines:
        # debug_info.append(f"Processing log line: {line}")
        match = log_pattern.match(line)
        # debug_info.append(f"Match: {match}")
        if match:
            log_timestamp = f"{match.group('month')} {match.group('day')} {match.group('hour')}:{match.group('minute')}:{match.group('second')}.{match.group('millisecond')}"
            # debug_info.append(f"Log timestamp: {log_timestamp}")
            log_time = parse_log_timestamp(log_timestamp)
            log_time = log_time.replace(year=now.year)
            # debug_info.append(f"Log time: {log_time}")
            if log_time >= time_threshold:
                recent_logs.append(line)
                # debug_info.append(f"Adding recent log: {line}")

    return recent_logs #, debug_info

class FilterModule(object):
    def filters(self):
        return {
            'filter_recent_logs': filter_recent_logs
        }