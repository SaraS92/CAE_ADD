import numpy as np
import os
import librosa
from librosa import display
from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import scipy.io.wavfile as wavfile
import wave
import re
import ffmpeg
import warnings
import pandas as pd
import matplotlib.pyplot as plt

"""
 This file is used for extracting 150 overlapping frames of raw audio signal samples with the sampling 
 rate of 1KHz.
"""
def make_frames(filename,folder,frame_length):
    num_frames=150
    filename = 'D:/dataset/samples_zeropad'+'/'+folder + '/'+filename
    data,sample_rate = librosa.load(filename,sr=1000)

    """
    # if you want to plot an audio signal you can use this code branch
    data_for_plot, sample_rate = librosa.load(filename, sr=1000,duration=5)
    plt.figure
    librosa.display.waveplot(y=data_for_plot,sr=sample_rate)
    plt.xlabel('time (seconds) --->')
    plt.ylabel('amplitude')
    
    """

    frame_length=frame_length*sample_rate

    colnames = range(0, frame_length)
    total_df=[]

    for i in range(0,int(num_frames)):
        temp =np.array([data[i:i+frame_length]])
        df = pd.DataFrame(temp, columns=colnames)
        total_df.append(df)

    new_df = pd.concat(total_df)

    return new_df

def make_frames_folder(folders,frame_length):

    for folder in folders:
        files = os.listdir('...'+'/'+folder)
        for file in files:
            res = make_frames(file,folder,frame_length)
            partic_id = os.path.basename(folder)
            nameid = re.sub('P', '', partic_id)
            nameid = int(nameid)
            filenm = str(nameid) + '.csv'
            output = '...' + filenm
            res.to_csv(output, index=False)
            del res
if __name__ == '__main__':
    frame_length = 4 #seconds to chunk with overlap

    dir_name = '...'# directory containing raw wav files after omitting second speaker
    out_dir = '...'
    folders = os.listdir('...')

    # train test dev split
    dataset_input_dir = '...'
    Train_file_name = dataset_input_dir + '...'
    Dev_file_name = dataset_input_dir + '...'
    Test_file_name = dataset_input_dir + '...'
    Train_files = pd.read_csv(Train_file_name)
    Dev_files = pd.read_csv(Dev_file_name)
    Test_files = pd.read_csv(Test_file_name)
    make_frames_folder(folders, frame_length)
