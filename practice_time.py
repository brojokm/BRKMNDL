import sys
from time import clock, sleep, time
def main():
	start_time = clock()
	sleep(3)
	end_time = clock()
	print(start_time)
	print(end_time)
	executeion_time = (end_time - start_time)
	print("Total time taken ") + str(executeion_time)

if __name__=="__main__":
	sys.exit(main())
