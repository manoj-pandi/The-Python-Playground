import  time

my_time = int(input("Enter the time in seconds: "))
# time.sleep(0, my_time)

for x in  reversed(range(0, my_time)):
    # print(x)
    seconds = x % 60
    minutes = int(x/ 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")