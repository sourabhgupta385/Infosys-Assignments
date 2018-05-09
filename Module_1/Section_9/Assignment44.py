'''
@author: SOURABH GUPTA
'''
'''
Execute the following code and observe the output.
1.import time
2.print(time.time())
3.print(time.localtime())
4.print(time.localtime(time.time()))
5.print(time.asctime())
6.mytime = (2016,7,27,15,45,23,0,0,0)
7.print(time.localtime(time.mktime(mytime)))
'''
import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
mytime = (2016,7,27,15,45,23,0,0,0)
print(time.localtime(time.mktime(mytime)))
