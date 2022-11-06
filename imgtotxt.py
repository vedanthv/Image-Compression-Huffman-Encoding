def imgtotxt(s):
	from PIL import Image
	from collections import Counter
	im=Image.open(s).convert('RGB')
	data=list(im.getdata())
	open('test1.txt','w')
	for i in data:
		for j in range(3):
			open('test1.txt','a').write(str(i[j])+'\n')
	f=open('test2.txt','w')
	with open('test1.txt', 'r') as fd:
		lines = fd.read().split()
		counter = Counter(lines)
		# sorts items
		items = sorted(counter.items(), key=lambda x: int(x[0]))
		# prints desired output
		for k, repetitions in items:
			f.write(str(k)+','+str(repetitions)+'\n')
	
	fd=open('test1.txt','a')
	fd.write(str(im.size))
