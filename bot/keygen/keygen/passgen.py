# /usr/bin/python3

import time, random, hashlib, pymysql, platform, os, sys, argparse

#pymysql will be for password sync
#next update will include a hash of hashes, and input date save to file function
def keygen():
 ### password option
 parser=argparse.ArgumentParser()
 parser.add_argument("-p","--password",help="optional password string")
 parser.add_argument("-c","--column",help="output data in column",action="store_true")
 options=parser.parse_args()
 delim="-"
 if options.column:
  numL=True
 else:
  numL=False

 if options.password:
  passString=str(options.password)
 else:
  passString=""
 
 passHash=hashlib.sha512()
 passHash.update(passString.encode())
 passFinal=passHash.hexdigest()
 ###
 ### local time string
 tacc=""
 
 for i in time.localtime():
  tacc=tacc+str(i)
 taccHash=hashlib.sha512()
 taccHash.update(tacc.encode())
 taccFinal=taccHash.hexdigest()
 ###
 ### local time list

 tac=list()
 
 for i in time.localtime():
  rtac=random.randint(0,i)
  
  tac.append(str(rtac))
 
 tacHash=hashlib.sha512()
 tacHash.update(''.join(tac).encode())
 tacFinal=tacHash.hexdigest()
 ## get username, get password
 ### get platform data
 unameHash=hashlib.sha512()
 unameHash.update(''.join(platform.uname()).encode())
 unameFinal=unameHash.hexdigest()
 ###
 ### combine data
 nonceTotal=tacFinal+taccFinal+" "+unameFinal+passFinal
 h=hashlib.sha512()
 h.update(nonceTotal.encode())
 ###
 result=h.hexdigest()
 breaker=8
 passAcc=""
 text=[result[i:i+breaker] for i in range(0,len(result),breaker)]
 for count,chunk in enumerate(text):
  if count < 15:    
   passAcc=passAcc+chunk+delim
  else:
   passAcc=passAcc+chunk
 if numL == True:
  data=passAcc.split(delim)
  print("Opt.#\tPassword\n=====\t========")
  for i,j in enumerate(data):
   print(i,j,sep="\t")
 else:
  data=passAcc
  print(data)
 return data

keygen()
