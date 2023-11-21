# CAE_ADD (Audio based depression detection using Convolutional Autoencoder)

This code is the implementation of the proposed idea published in th following paper: https://doi.org/10.1016/j.eswa.2021.116076

The paper proposes an automatic depression detection system in which the model is trying to detect depression through audio samples. For further discussion over the results and contributions please check the associated paper.

The code includes several partsa of preprocessing such as speaker segmentation, silence removal and in some cases extracting features of OpenSMILE. The implementation of the model includes:

. A simple dense AutoEncoder for automatic feature extraction

. The convolutional AutoEncoder for automatic feature extraction

It is worth mentioning that for some parts of the code in preprocessing we used (and slightly changed) the preprocessing stage mentioned in : https://github.com/kykiefer/depression-detect
