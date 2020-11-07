data=[]
count = 0
sum_length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print('讀取進度', len(data)/10000, '%')
print('檔案讀取完畢,共', len(data), '筆資料')

for message in data:
	sum_length = sum_length + len(message)
average_length = sum_length / len(data)
print('總字數:', sum_length, '字')
print('每筆留言平均字數:', average_length, '字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言,長度小於100')


good= []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')

new1 = [1 for d in data if 'good' in d]
print(len(new1))

keyword_number = input('想查詢出現幾次以上的關鍵字呢? :')

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] = wc[word] + 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > int(keyword_number):
		print(word, wc[word])

print('總共有:', len(wc), '個不同的字')

while  True:
	keyword = input('請輸入想查詢的關鍵字:')
	if keyword == 'q':
		break
	if keyword in wc:
		print(keyword, '出現的次數為:', wc[keyword])
	else:
		print(keyword + '沒有出現過喔!')

print('感謝您使用本查詢功能')
