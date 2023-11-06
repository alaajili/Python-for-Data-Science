from datetime import datetime

current_timestamp = datetime.now().timestamp()

print(f'Seconds since January 1, 1970: {current_timestamp:,.4f} or {current_timestamp:.2e} in scientific notation')

current_date = datetime.now()

print(current_date.strftime("%b %d %Y"))