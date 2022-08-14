import os
prdts = []
if os.path.isfile('prdts.csv'):
	print('yea! find')
	with open ('prdts.csv', 'r', encoding='utf-8') as f :
		for line in f :
			if '商品，價格' in line:
				continue
		n, p = line.strip().split(',')
		prdts.append([n, p])
	print(prdts)
else:
	print('no find')



#讓使用者輸入
while True:
	n = input("請輸入商品名稱 :")
	if n == 'q' :
			break
	p = input("請輸入商品價格 :")
	p = int(p)
	prdts.append([n,p])
print(prdts)

#印出所有購買紀錄
for p in prdts :
	print(p[0], "的商品價格為", p[1])

#寫入檔案
with open ("prdts.csv","w",encoding="utf-8") as f :
	f.write("商品, 價格\n")
	for p in prdts :
		f.write(p[0] + "," + str(p[1]) + "\n")
