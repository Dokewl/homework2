import time
def calculate_time(func):
	current_time = time.time()
	def wrapper():
		print("Printed immediately")
		print(current_time)
		func()
		print("Printed after sleep")
	return wrapper
@calculate_time()
def sleep_time():
	time.sleep(2)
sleep_time = calculate_time(sleep_time)


