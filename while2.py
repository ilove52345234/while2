
x = 3
while x <= 3:
	password = input('請輸入密碼: ')
	x = x - 1
	if password != 'a123456' and x > 0:
		print('密碼錯誤還有', x, '次機會')
	elif password == 'a123456':
		print('登入成功')
		break
	elif x == 0:
		break
