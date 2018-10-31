>>> import numpy as np
>>> import pandas as pd
>>> import os
>>> os.chdir('/home/aravind/Desktop')
>>> files = pd.read_csv("table1.csv")
>>> files2 = pd.read_csv("table2.csv")
>>> files2
   u_id        email  age
0     1  a@gmail.com   23
1     2   b@mail.com   43
2     3  d@gmail.com   43
>>> files
   u_id  a_id  add
0     1     2    3
1     1    23    4
2     2    34    5
3     2     4    5
4     6     7    8
5     4     8    4
6    99     7    6
>>> m = pd.merge(files, files2, on='u_id')
>>> m
   u_id  a_id  add        email  age
0     1     2    3  a@gmail.com   23
1     1    23    4  a@gmail.com   23
2     2    34    5   b@mail.com   43
3     2     4    5   b@mail.com   43
