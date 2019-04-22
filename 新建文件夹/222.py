import re
a='utc+5:00'
u=re.match(r'(utc|UTC)[+|-](\d):00',a).group(2)