from email import header
from gc import callbacks
from time import sleep
from tokenize import group
from unittest import result
from celery import *

from task import *


#---chain-----
# lst=[45, 78 , 10 , 20]
# task=chain(addition.s(lst[0],lst[1]),addition.s(lst[2]),addition.s(lst[3])).apply_async()
# while True:
#     print(task.get())
#     exit()



#------groups-----
# tskLst=[]
# lst=[45, 78 , 10 , 20]
# for _ in range(4):
#     tskLst.append(a_min.s(lst[_]))

# result= group(tskLst).apply_async()

# if result.ready:
#     print(result.get())
#     exit()


#-----chords----
callback = pnt.s()
header = [addition.s(i, i) for i in range(10000)]
result = chord(header)(callback)
print(result.get())



