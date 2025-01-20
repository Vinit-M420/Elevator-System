import time

# Set the time limit in seconds and the number of repetitions
time_limit = 5  # Change this to your desired time limit
repetitions = 10  # Number of times to print the message

for _ in range(repetitions):
    print("This message is printed every", time_limit, "seconds.")
    time.sleep(time_limit)  # Wait for the specified time limit
