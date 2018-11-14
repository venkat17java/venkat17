bicycles = ['Mtb','Atlas','2']
print("This bicycle number is "+bicycles[-1].title())

motorCycles = ['honda','yamaha','suzuki']
print(motorCycles)

motorCycles.append('ducati')
motorCycles.insert(0,'jeep')
del motorCycles[3]

popped_motorCycle = motorCycles.pop()
print(popped_motorCycle)
print(motorCycles)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	
	print("Thank you everyone, that was a great magic show!")