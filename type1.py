import os

# 讀檔
def read_file(address='input.txt'):
	data = []
	if os.path.isfile(address):
		with open(address, 'r', encoding = 'utf-8-sig') as f:
			for line in f:
				data.append(line.strip())
		return data
	else:
		print('找不到對話檔案')
# 轉換資料
def convert(chat, p1, p2):
	talker = None
	new = []
	for c in chat:
		if c == p1:
			talker = p1
			continue
		elif c == p2:
			talker = p2
			continue
		else:
			new.append(talker + ': ' + c)
	print('轉換完成')
	return new
# 存檔
def write_file(output, address='output.txt'):
	with open(address, 'w', encoding = 'utf-8-sig') as f:
		for line in output:
			f.write(line + '\n')

def main():
	raw = read_file()
	if raw:
		output = convert(raw, 'Allen', 'Tom')
		write_file(output, 'result.txt')

if __name__ == '__main__':
	main()




	