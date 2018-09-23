lenghtstr = 0
words_pack = 0
with open('referat.txt', 'r', encoding = 'utf-8') as f:
	for line in f:
		lenghtstr = lenghtstr + len(line)
		words_pack = words_pack + len(line.split(' '))
		line = line.replace(',','!')
		with open('referat2.txt', 'a', encoding = 'utf-8') as d:
			d.write(line)

print(lenghtstr)
print(words_pack)