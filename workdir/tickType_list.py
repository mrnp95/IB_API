from ibapi.ticktype import TickTypeEnum

for i in range(105):
	print(TickTypeEnum.to_str(i), i)