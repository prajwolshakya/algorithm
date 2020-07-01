def wrong():
	num, k = input().split()
	# k =
	num=int(num)
	k = int(k)
	for i in range(0, k):
		if num % 10 == 0:
			num = num/10
		else:
			num = num -1
	print(num)
def main():
	wrong()

if __name__ == "__main__":
	main()