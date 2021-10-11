import time

start_time1 = time.time()

for x in range(10000):
    x = []
    for i in range(10):
        x += [1]
        
print((time.time() - start_time1)/10000)

start_time2 = time.time()

for x in range(10000) :
    x = []
    for i in range(10):
        x.append(1)
        
print((time.time() - start_time2)/10000)