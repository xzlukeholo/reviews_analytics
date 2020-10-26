data=[]
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print('讀取進度', len(data)/10000, '%')
print('共', len(data), '筆資料')