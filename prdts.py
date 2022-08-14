prdts = []
while True:
	n = input("請輸入商品名稱 :")
	if n == 'q' :
			break
	p = input("請輸入商品價格 :")
	prdts.append([n,p])
print(prdts)

for p in prdts :
	print(p[0],"的商品價格為",p[1])

with open ("prdts.txt","w") as f :
	for p in prdts :
		f.write(p[0] + "," + p[1] + "\n")

with open ("prdts.csv","w",encoding="utf-8") as f :
	f.write("商品, 價格\n")
	for p in prdts :
		f.write(p[0] + "," + str(p[1]) + "\n")