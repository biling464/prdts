prdts = []
while True:
	n = input("請輸入商品名稱 :")
	if n == 'q' :
			break
	p = input("請輸入商品價格 :")
	prdts.append([n,p])
print(prdts)


