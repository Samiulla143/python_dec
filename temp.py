import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i} from {threading.current_thread().name}")
        time.sleep(1)  # Simulate a delay

# Task 2: Print letters
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter} from {threading.current_thread().name}")
        time.sleep(1.5)  # Simulate a delay

# Create threads
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_letters, name="Thread-2")

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have completed their tasks.")q