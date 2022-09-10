from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for x in range(10):
            print('hello')
            sleep(1)

class hi(Thread):
    def run(self):
        for y in range(5):
            print('hi')
            sleep(1)

h1=hello()
h2=hi()

h1.start()
sleep(0.5)
h2.start()
#here if we directly run print(bye)command then we will get it in bw hence to avoid that we will use join that means the process running on different threads wil be completely executrd and then we will let the two threads join and then we will print bye

h1.join()
h2.join()
print('bye')
#so here we are using multi threading running two process in parallel
#we are giving a sleep command as the cpu runs super fast 
 