from enum import Enum

month=Enum('month',('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))

for name,member in month.__members__.items():
    print(name,'=>',member,',',member.value)

#value自动付给成员int属性，默认从1开始