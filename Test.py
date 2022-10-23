# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:16:16 2022

@author: Zihao Wang

A testing file consists of some simple code blocks for different purpose.
"""


#%% Test count and KeyboardInterrupt of a while loop
import time

interval_seconds = 3

word = 'Hello'
name = 'Zihao'

count = 0

def seyhello(word, name, count=0):
    count += 1
    print(word + '!' + name + f'+{count}')
    return count

while count < 200:
    try:
        count = seyhello(word, name, count)
        time.sleep(2)
    except KeyboardInterrupt:
        print('Thank you, have a FANTASTIC day!')
        break
    
    
    
#%% Test how yaml works
from ruamel.yaml import YAML

yaml = YAML()
with open('OvernightScanParams.yaml') as file:
    yaml_params = yaml.load(file)    

result = dict(yaml_params['Q0']['01']['T1'])  
    
print(result)
    
    
    
#%% Test super.()
# Reference: https://realpython.com/python-super/

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    def tri_area(self):
        return 0.5 * self.base * self.height    
    
    
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)
        super().__init__(self.base, self.slant_height)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area    
    
class MyPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        Square.__init__(self, length=base)
        Triangle.__init__(self, base=slant_height, height=slant_height)
    
    
    
#%% Test dependency Injection
# Reference: https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl/33469090#33469090

class SomeBaseClass(object):
    def __init__(self):
        print('SomeBaseClass.__init__(self) called')
    
class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print('UnsuperChild.__init__(self) called')
        SomeBaseClass.__init__(self)
    
class SuperChild(SomeBaseClass):
    def __init__(self):
        print('SuperChild.__init__(self) called')
        super().__init__()

class InjectMe(SomeBaseClass):
    def __init__(self):
        print('InjectMe.__init__(self) called')
        super().__init__()

class UnsuperInjector(UnsuperChild, InjectMe): pass

class SuperInjector(SuperChild, InjectMe): pass



#%% Test warning.warn
# Reference: https://stackoverflow.com/questions/60083173/warnings-module-prints-part-of-warning-twice
# You can try to play with the stacklevel to learn more!

import warnings

target = 2

def compare(number):
    if number > target:
        warnings.warn(f'The number {number} is too high', stacklevel=2)
    else:
        print('Test pass.')



#%% Test multiple plot

import matplotlib.pyplot as plt
import numpy as np

testlist = np.random.normal(2, 0.5, 100)

fig, axes = plt.subplots(2, 2, figsize=(16,16), squeeze=False)
n, bins, patches = axes[0][1].hist(testlist, color='indigo', 
                                   alpha=0.35, rwidth=0.8)   
fig.show()

fig, axes = plt.subplots(2, 2, figsize=(16,16), squeeze=False)
n, bins, patches = axes[1][0].plot(testlist, color='indigo', alpha=0.35)   

fig.show()


#%% Test defining a function with particular data type / return type

def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    print(type(num1))
    return num3
 
# Driver code
num1, num2 = 5.2, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

'''
My conclusion is there is just no difference. If we infer the type of data,
it will be more readable. Check PEP 483.
'''


#%% Transform a jpg image into grayscale pixel array. Also some simple image processing.
# Ref:https://www.bilibili.com/video/BV1Wy4y1h7ii?spm_id_from=333.999.0.0&vd_source=c9ac22d57714338bf6390a2064e93622

from PIL import Image

im1 = Image.open(r'E:\OneDrive\OneDrive - University of Rochester\others\Photo_Zihao_Wang.jpg')
im2 = Image.open(r'E:\OneDrive\OneDrive - University of Rochester\others\_MG_5415.JPG')
# im.show()

gs1 = np.array(im1)   # Make it nparray.
gs1_r = gs1[:,:,0]   # Get its red component.
# Image.fromarray(gs1_r).show()  # Plot the red component grayscale.

gs2 = np.array(im2)
gs_combine = 0.5*gs1[0:4640, 0:4006, :] + 0.5*gs2[0:4640, 2500:6506, :]
gs_combine = gs_combine.astype(np.uint8)
Image.fromarray(gs_combine).show()


#%% Zen of Python
import this


#%% About 'yield' and generator.
# Ref: https://www.bilibili.com/video/BV1kT4y1u72i?spm_id_from=333.999.0.0&vd_source=c9ac22d57714338bf6390a2064e93622

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a 
        a, b = b, a + b

for i in fibonacci(10):
    print(i)

print(f'The type of fibonacci(10) here is {type(fibonacci(10))}')

# The good point here is we don't need to wait until all loop finish.
# Every time the loop run, it pop up a result that will be printed.


#%% Test np.argsort()
import numpy as np

testlist = [[7, 3, 5, 2], [43, 11, 22, 65]]
result = np.argsort(testlist, 1)

print(result)
print(type(result))


#%%





























