x = 3
pwd = 'a123456'
while x > 0:
	password = input('請輸入密碼: ')
	x = x - 1
	if password == pwd:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if x > 0:
			print('還有', x, '次機會')
		else:
			print('請聯絡客服人員!')