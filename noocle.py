#argvs[1] is time to complete making something
import sys
import time

argvs = sys.argv
noodle_time_min=float(argvs[1])
noodle_time_sec=noodle_time_min*60
print(noodle_time_sec)
boot_time=time.time()
while(1):
    elapsed_time=time.time()-boot_time
    if elapsed_time > noodle_time_sec:
        print('completed noodle')
        break


