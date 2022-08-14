import os
def  read_file(filename):
	prdts = []
	with open (filename, 'r', encoding='utf-8') as f :
		for line in f :
			if '商品，價格' in line:
				continue
		n, p = line.strip().split(',')
		prdts.append([n, p])
	return prdts

#讓使用者輸入
def user_input(prdts):
	while True:
		n = input("請輸入商品名稱 :")
		if n == 'q' :
				break
		p = input("請輸入商品價格 :")
		p = int(p)
		prdts.append([n,p])
	print(prdts)
	return prdts

#印出所有購買紀錄
def print_products(prdts):
	for p in prdts :
		print(p[0], "的商品價格為", p[1])

#寫入檔案
def write_file(filename, prdts):
	with open (filename,"w",encoding="utf-8") as f :
		f.write("商品, 價格\n")
		for p in prdts :
			f.write(p[0] + "," + str(p[1]) + "\n")

def main():
	filename = 'prdts.csv'
	if os.path.isfile(filename):
		print('yea! find')
		prdts = read_file(filename)
	else:
		print('no find')
	prdts = user_input(prdts)
	print_products(prdts)
	write_file('prdts.csv',prdts)

main()