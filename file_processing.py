import os
import numpy as np

def showData(data, names):
    i = 0
    while i < data.shape[0]:
        print(names[i] + ": ")
        j = 0
        while j < data.shape[1]:
            print(data[i][j])
            j += 1
        print("")
        i += 1

def Main():
    print("The sample data is: ")
    fname = 'data.csv'
    csv = np.genfromtxt(fname, dtype=str, delimiter=",")
    num_rows = csv.shape[0] # x axis in graphics computer
    num_cols = csv.shape[1] # y axis in graphics computer
    names = csv[1:,0]
    # get data frame from the first column to the end colums
    data = np.genfromtxt(fname, usecols = range(1,num_cols), delimiter=",")
    print(names)
    print(str(num_rows) + "x" + str(num_cols))
    print(data)
    showData(data, names)
    
 
#The sample data is:
#['CONFIG000' 'CONFIG001' 'CONFIG010' 'CONFIG011' 'CONFIG100' 'CONFIG101'
# 'CONFIG110' 'CONFIG111']
#8x9
#[[ 1080.65  1080.87  1068.76  1083.52  1084.96  1080.31  1081.75  1079.98]
# [  414.6    421.76   418.93   415.53   415.23   416.12   420.54   415.42]
# [ 1091.43  1079.2   1086.61  1086.58  1091.14  1080.58  1076.64  1083.67]
# [  391.31   392.96   391.24   392.21   391.94   392.18   391.96   391.66]
# [ 1067.08  1062.1   1061.02  1068.24  1066.74  1052.38  1062.31  1064.28]
# [  371.63   378.36   370.36   371.74   370.67   376.24   378.15   371.56]
# [ 1060.88  1072.13  1076.01  1069.52  1069.04  1068.72  1064.79  1066.66]
# [  350.08   350.69   352.1    350.19   352.28   353.46   351.83   350.94]]

#CONFIG000:
#1080.65
#1080.87
#1068.76
#1083.52
#1084.96
#1080.31
#1081.75
#1079.98

#CONFIG001:
#414.6
#421.76
#418.93
#415.53
#415.23
#416.12
#420.54
#415.42

#CONFIG010:
#1091.43
#1079.2
#1086.61
#1086.58
#1091.14
#1080.58
#1076.64
#1083.67

#CONFIG011:
#391.31
#392.96
#391.24
#392.21
#391.94
#392.18
#391.96
#391.66

#CONFIG100:
#1067.08
#1062.1
#1061.02
#1068.24
#1066.74
#1052.38
#1062.31
#1064.28

#CONFIG101:
#371.63
#378.36
#370.36
#371.74
#370.67
#376.24
#378.15
#371.56

#CONFIG110:
#1060.88
#1072.13
#1076.01
#1069.52
#1069.04
#1068.72
#1064.79
#1066.66

#CONFIG111:
#350.08
#350.69
#352.1
#350.19
#352.28
#353.46
#351.83
#350.94
