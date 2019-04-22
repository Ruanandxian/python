from enum import Enum, unique


@unique
class weekday(Enum):
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fir = 5
    sat = 6


day1 = weekday.mon

print('day1=', day1)
print('weekday.tue=', weekday.tue)
print('weekday[\'tue\']=', weekday['tue'])
print('weekday.tue.value=', weekday.tue.value)
print('day1==weekday.mon?', day1 == weekday.mon)
print('day1==weekday.tue?', day1 == weekday.tue)
print('day1==weekday(1)?', weekday(1))

for name, member in weekday.__members__.items():
    print(name, '>=', member)
