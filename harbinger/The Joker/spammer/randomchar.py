#! /usr/bin/python3
import random, tarfile, time


class stringy():
 
 string=list()
 #ascii range
 upper=127
 lower=32
 #string length
 strlen=8
 accI=str()
 iterations=int()
 def __init__(self):
  for i in time.localtime():
   self.accI+=str(i)
  self.iterations=random.randint(0,int(self.accI))

 #generate a random string
 def randomchar(self):
  for i in range(0,self.strlen):
   self.string.append(chr(random.randint(self.lower,self.upper)))
  
  return ''.join(self.string)
 # generate a random string using self.iterations, due to time taken to generate string, might use this as a cpu spammer
 # if that is the case, get ram size, make a function that then uses up to 80% of ram using gen()
 # make a another function to open two sockets, one dest and one src, send text data generated by randomchar() from one socket to other over network
 #  as a network spammer, flooder
 # make a function to fork bomb the user of this script
 # make another function to randomly choose which bomb to open
 # see about making a function that causes a harmless, but still startling BSOD to windows systems
 def gen(self):
  for i in range(0,self.iterations):
   result=self.randomchar()
  return result

a=stringy()
b=a.randomchar()
print(b)
