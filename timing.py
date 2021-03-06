import time
def calculate_time(func):
	""" Decorator, Calculates the time it takes to run. """
	def wrapper():
		time1 = time.time()
		func()
		time2 = time.time()
		x = time2 -time1
		print(f"Total time {x}")
	return wrapper
@calculate_time
def sleep_time():
	""" Function that makes the program sleep for 2 seconds. """
	time.sleep(2)
if __name__ == '__main__':
	myfunc()


