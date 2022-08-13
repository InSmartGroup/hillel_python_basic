import time

start = time.time()

counter = 0

while True:
    counter += 1
    if counter == 1_000_000:
        break

print(time.time() - start)
