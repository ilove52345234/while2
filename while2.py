x = 3
pwd = 'a123456'
while True:
	password = input('請輸入密碼: ')
	x = x - 1
	if password != pwd and x > 0:
		print('密碼錯誤還有', x, '次機會')
	elif password == pwd:
		print('登入成功')
		break
	elif x == 0:
		break
