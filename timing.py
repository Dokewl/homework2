import time
def calculate_time(func):
	def wrapper():
		print("Printed immediately")
		print(current_time)
		func()
		print("Printed after sleep")
	return wrapper
def sleep_time():
	current_time = time.time()
	time.sleep(2)
sleep_time = calculate_time(sleep_time)


