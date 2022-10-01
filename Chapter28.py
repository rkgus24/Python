a = input().split(" ") 
type(a)

x = int(a[0]); op = a[1]; y = int(a[2])

def cal(a, op, b):
	if op == "+" : print(f'{a} {op} {b} = {a + b}')
	elif op == "-" : print(f'{a} {op} {b} = {a - b}')
	elif op == "*" : print(f'{a} {op} {b} = {a * b}')
	elif op == "/" : print(f'{a} {op} {b} = {a / b}')
	
cal(x, op, y)
