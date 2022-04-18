import os
LINE_friend = "Chou²'s RJ"

# 讀檔
def read_file(address):
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
	fuc_count_p1 = 0
	fuc_count_p2 = 0
	call_time = 0
	fuck = '笨'
	new = []
	time = None
	name = None
	for line in chat:
		if '（週' in line:
			new.append(line)
			continue
		if '通話時間' in line:
			t = line.strip().split('	')
			t = t[2].split(' ')
			t = t[1].split(':')
			if len(t) == 3:
				call_time += int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])
			elif len(t) == 2:
				call_time += int(t[0]) * 60 + int(t[1])
		s = line.strip().split('	')
		if len(s) > 2:
			time = s[0]
			name = s[1]
			if len(s) > 3:
				for m in s[3:]:
					s[2] += m
			# 聊天計數
			if p1 or p2 in s:
				if name == p1:
					if '[貼圖]' in s[2]:
						sticker_count_p1 += 1
					elif '[照片]' in s[2]:
						pic_count_p1 += 1
					else:
						word_count_p1 += len(s[2])
					if fuck in s[2]:
						fuc_count_p1 += 1
				elif name == p2:
					if '[貼圖]' in s[2]:
						sticker_count_p2 += 1
					elif '[照片]' in s[2]:
						pic_count_p2 += 1
					else:
						word_count_p2 += len(s[2])	
					if fuck in s[2]:
						fuc_count_p2 += 1		
				new.append([time, name, s[2]])
		elif s:
			new.append([time, name, s[0]])
	c_hour = (int)(call_time / 3600)
	c_sec = call_time % 60
	c_min = (call_time - c_sec) / 60 - c_hour * 60
	print('...轉換完成!')
	print(p1, '說了', word_count_p1, '個字')
	print(p1, '傳了', sticker_count_p1, '個貼圖')
	print(p1, '傳了', pic_count_p1, '張圖片')
	print(p1, '說了', fuc_count_p1, '次', fuck)
	print(p2, '說了', word_count_p2, '個字')	
	print(p2, '傳了', sticker_count_p2, '個貼圖')	
	print(p2, '傳了', pic_count_p2, '張圖片')
	print(p2, '說了', fuc_count_p2, '次', fuck)
	print('總通話時間', '%i'%c_hour, '小時', '%i'%c_min,'分', '%i'%c_sec,'秒')
	return new

# 存檔
def write_file(output, address='output.txt'):
	time = None
	talker = None
	with open(address, 'w', encoding = 'utf-8-sig') as f:
		for line in output:
			if '（週' in line:
				f.write('====================\n' + line + '\n')
				continue
			if line[0] == time and line[1] == talker:				
				f.write(line[2] + '\n')				
			else:
				f.write('\n' + line[0] + ' ' + line[1] + ':\n')
				f.write(line[2] + '\n')
				time = line[0]
				talker = line[1]


def main():
	raw = read_file("[LINE] 與" + LINE_friend + "的聊天.txt")
	if raw:
		output = convert(raw, LINE_friend, 'Eric')
		write_file(output, 'result_LINE_' + LINE_friend + '.txt')

if __name__ == '__main__':
	main()




	