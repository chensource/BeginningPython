from multiprocessing import Pool
import time
import random
import os
import subprocess


#子进程要执行的代码
def run_proc(name):
    print("Run child process %s (%s)" % (name, os.getpid()))


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f secondes" % (name, (end - start)))

# if __name__ == "__main__":
# print("Parent process %s " % (os.getpid()))
# p = Process(target=run_proc, args=('test', ))
# p = Process(target=run_proc, args=(q,))
# p = process()
# print("Child process will start.")
# p.start()
# p.join()
# print("Child process end.")

# print("Parent process %s " % (os.getpid()))
# # print(process.__file__)
# p = Pool(4)
# for i in range(5):
#     p.apply_async(long_time_task, args=(i, ))
# print("Waiting for all subprocess done...")
# p.close()
# p.join()
# print("all subprocess done.")

print("nslookup")
p = subprocess.Popen(['nslookup'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('exit code:', p.returncode)
