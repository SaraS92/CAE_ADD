import pandas as pd
import csv
import numpy as np
import os
import re
"""
This part of code extracts the first 150 samples of each opensmile feature set for each audio
 
"""

def nonrandom_split (data,samplenum,filename):
    for name, df_name in data.groupby('name'):
        if (len(df_name.index) < samplenum):
            df = df_name
        else:
            df = df_name.head(samplenum)
        filenm = str(name) + '.csv'
        output = '...' + filenm
        df.to_csv(output, index=False)


if __name__ == '__main__':
    dataset_input_dir = '...'
    Train_file_name = dataset_input_dir + '...'
    Dev_file_name = dataset_input_dir + '...'
    Test_file_name = dataset_input_dir + '...'
    Testfiles = pd.read_csv(Test_file_name, sep=",")
    Trainfiles = pd.read_csv(Train_file_name, sep=",")
    Devfiles = pd.read_csv(Dev_file_name, sep=",")

    #uncomment for saving each file
    Devdata=nonrandom_split(Devfiles,150,'dev')
    #Devdata.to_csv('...', index=False)
    Testdata = nonrandom_split(Testfiles, 150,'test')
    #Testdata.to_csv('...', index=False)
    Traindata = nonrandom_split(Trainfiles, 150,'train')
    #Traindata.to_csv('...', index=False)

