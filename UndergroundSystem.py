class UndergroundSystem(object):

	def __init__(self):
		self.d = {}

	def checkIn(self, id, stationName, t):
		self.d[id]= {'id': id,'station_in':stationName,'station_out':'','tin':t,'tout': 0,'active':'1'}
		# print(self.d[id])

	def checkOut(self, id, stationName, t):
		if id in self.d.keys() and self.d[id]['station_in'] != stationName:
			self.d[id]['station_out']= stationName
			self.d[id]['tout'] = t
			self.d[id]['active'] = 0
			self.d[id]['diff'] = self.d[id]['tout'] - self.d[id]['tin']

	def getAverageTime(self, startStation, endStation):
		# print(self.d)
		count,total = 0,0
		for key, val in self.d.items():

			if val['station_in'] == startStation and val['station_out'] == endStation:
				count = count + 1
				start =  self.d[val['id']]['tin']
				end =  self.d[val['id']]['tout']
				assert end>start
				total += end - start
				# print(end)
		return  total/count



	
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(45, "Leyton", 8)

undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo")  )
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))

# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3] c
# 	,[32,"Paradise",8],c
#  [27,"Leyton",10],c
#  [45,"Waterloo",15],o
#  [27,"Waterloo",20],0
#  [32,"Cambridge",22]0
# 	,["Paradise","Cambridge"]
# 	,["Leyton","Waterloo"]
# 	,[10,"Leyton",24]c
# 	,["Leyton","Waterloo"]
# 	,[10,"Waterloo",38]
# 	,["Leyton","Waterloo"]]
