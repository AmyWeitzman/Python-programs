import re
date= 'Barca 2019-04-21'
match=re.search('(\S+) (\d+)-(\d+)-(\d+)',date)
if match:
    print(match.groups())
    print(type(match.groups()))
