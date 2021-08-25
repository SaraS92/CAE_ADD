
import warnings
import librosa
import opensmile
import pandas as pd
import csv
import numpy as np
import os
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import scipy.io.wavfile as wavfile
import re

"""
This file is used to extract opensmile features out of each audio file.

"""


#main
if __name__ == '__main__':
    """
    #To use the opensmile, you can uncomment this branch of code
    
    dir_name = '...'#audio files after omitting the second speaker
    out_dir = '...'
    
    for subdir, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith('.wav'):
                input_filepath = os.path.join(subdir, file).replace("\\", "/")
                partic_id = os.path.basename(subdir)
                sample_dir = os.path.join(out_dir, partic_id).replace("\\", "/")
                if not os.path.exists(sample_dir):
                    os.makedirs(sample_dir)
                os.chdir(sample_dir)
                instname = os.path.splitext(file)[0]
                outfilepath = sample_dir + '/'  + instname + '.csv'
                
                #opensmile command
                opensmile_call = 'SMILExtract'+' '+'-C'+' '+'config/avec11-14/avec2013.conf'+' '+'-I'+' '+input_filepath+' '+'-csvoutput'+' '+outfilepath
                #'SMILExtract -C config/avec11-14/avec2013.conf -I 300_AUDIO.WAV -csvoutput 300_AUDIOtest.csv'
                os.system('cd D:\\opensmile-3.0-win-x64\\bin && ' + opensmile_call)
    """
    #train test dev split
    dataset_input_dir='...'
    Train_file_name=dataset_input_dir+'...'
    Dev_file_name = dataset_input_dir + '...'
    Test_file_name = dataset_input_dir + '...'
    Train_files = pd.read_csv(Train_file_name)
    Dev_files = pd.read_csv(Dev_file_name)
    Test_files = pd.read_csv(Test_file_name)

    #concatenate csv files
    dir_name = '...'
    TrainList = []
    TestList = []
    DevList = []
    for subdir, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith('.csv'):
                filename = os.path.join(subdir, file).replace("\\", "/")
                fixed_files = pd.read_csv(filename, sep=";")
                partic_id = os.path.basename(subdir)
                nameid= re.sub('P', '',  partic_id)
                nameid=int(nameid)
                fixed_files = fixed_files.assign(name=nameid)

                if(Train_files[Train_files['Participant_ID']==nameid].index.tolist()):
                    listindex=Train_files[Train_files['Participant_ID']==nameid].index.tolist()
                    temp = Train_files.iloc[listindex]
                    index = list(temp.index)
                    label = temp.loc[index[0], 'PHQ8_Binary']
                    fixed_files['Class'] = label
                    TrainList.append(fixed_files)

                    #PHQ8_Binary
                elif(Test_files[Test_files['Participant_ID']==nameid].index.tolist()):
                    listindex = Test_files[Test_files['Participant_ID'] == nameid].index.tolist()
                    temp = Test_files.iloc[listindex]
                    index = list(temp.index)
                    label = temp.loc[index[0], 'PHQ_Binary']
                    fixed_files['Class'] = label
                    TestList.append(fixed_files)
                else:
                    listindex = Dev_files[Dev_files['Participant_ID'] == nameid].index.tolist()
                    temp = Dev_files.iloc[listindex]
                    index = list(temp.index)
                    label = temp.loc[index[0], 'PHQ8_Binary']
                    fixed_files['Class'] = label
                    DevList.append(fixed_files)

        #if(len(TrainList)!=0 &len(TestList)!=0 &len(DevList)!=0):
    new_Train = pd.concat(TrainList)
    new_Test = pd.concat(TestList)
    new_Dev = pd.concat(DevList)

    new_Train.to_csv('...', index=False)
    new_Test.to_csv('...', index=False)
    new_Dev.to_csv('...', index=False)
