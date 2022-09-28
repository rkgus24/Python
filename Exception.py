try:
	print("나누기 전용 계산기입니다.")
	nums = [] # 0 서랍이 없어서 값을 넣을 수 없다
	nums.append(int(input("첫 번째 숫자를 입력하세요 : "))) # append를 이용해서 서랍을 만들어 준다
	nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
	# nums.append(int(nums[0] / nums[1]))
	print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
	print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
	print(err)
except Exception as err: #나머지 에러
	print("알 수 없는 에러가 발생하였습니다.")
	print(err)