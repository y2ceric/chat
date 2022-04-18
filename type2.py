import os

# 讀檔
def read_file(address='LINE-Viki.txt'):
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
	word_count_p1 = 0
	word_count_p2 = 0
	sticker_count_p1 = 0
	sticker_count_p2 = 0
	pic_count_p1 = 0
	pic_count_p2 = 0
	new = []
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		# 聊天計數
		if name == p1:
			if s[2] == '貼圖':
				sticker_count_p1 += 1
			elif s[2] == '圖片':
				pic_count_p1 += 1
			else:
				for m in s[2:]:
					word_count_p1 += len(m)
		elif name == p2:
			if s[2] == '貼圖':
				sticker_count_p2 += 1
			elif s[2] == '圖片':
				pic_count_p2 += 1
			else:
				for m in s[2:]:
					word_count_p2 += len(m)
		# 聊天還原
		if len(s) > 3:
			for m in s[3:]:
				s[2] += m
		new.append([time, name, s[2]])
	print('...轉換完成!')
	print(p1, '說了', word_count_p1, '個字')
	print(p1, '傳了', sticker_count_p1, '個貼圖')
	print(p1, '傳了', pic_count_p1, '張圖片')
	print(p2, '說了', word_count_p2, '個字')	
	print(p2, '傳了', sticker_count_p2, '個貼圖')	
	print(p2, '傳了', pic_count_p2, '張圖片')
	return new

# 存檔
def write_file(output, address='output.txt'):
	time = None
	talker = None
	with open(address, 'w', encoding = 'utf-8-sig') as f:
		for line in output:
			if line[0] == time and line[1] == talker:				
				f.write(line[2] + '\n')				
			else:
				f.write(line[0] + ' ' + line[1] + ':\n')
				f.write(line[2] + '\n')
				time = line[0]
				talker = line[1]


def main():
	raw = read_file()
	if raw:
		output = convert(raw, 'Allen', 'Viki')
		write_file(output, 'result_Line.txt')

if __name__ == '__main__':
	main()




	