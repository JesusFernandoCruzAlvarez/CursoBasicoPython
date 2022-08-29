#ciclos en python
i=0
while i<10:
	i+=1 
	print(i)
#Uso de continue
i=0
while i<10:
	i+=1 
	if i==7:
		continue
	print(i)
#Uso de break
i=0
while True:
	i+=1
	print(i)
	if i==13:
		break
