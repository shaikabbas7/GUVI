while True:
	try:
		x,y= raw_input().split()
		x=int(x)
		y=int(y)
		break
	except:
		print("Invalidinput")
		break
z=1
for x in range(y):
	z=z*x
print(z)
