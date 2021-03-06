import time
def calculate_time(func):
""" Decorator, calculates the amount of time to run. """
	def wrapper():
		time1 = time.time()
		func()
		time2 = time.time()
		x = time2 -time1
		print(f"Total time {x}")
	return wrapper
@calculate_time
def sleep_time():
""" Function to go to sleep for 2 seconds. """
	time.sleep(2)
if __name__ == '__main__':
	myfunc()


