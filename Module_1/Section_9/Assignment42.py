'''
@author: SOURABH GUPTA
'''
'''
If area of one wall of a cubical wooden box is 16 units, write a Python program to display the volume of the box. 
'''
import math
area = 16
side = math.sqrt(area)
print("Volume is : ", math.pow(side, 3))
