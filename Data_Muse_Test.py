# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:20:21 2021

@author: Myriam
"""

import pyxdf
import os
import os.path as op
import numpy as np
import mne
from mne.datasets import misc

fname1=op.join(misc.data_path(), 'xdf', 'Sans_tête.xdf')

streams1, header1 = pyxdf.load_xdf(r'C:\Users\Myriam\Documents\CurrentStudy\sub-P001\ses-S001\eeg\Sans_tête.xdf')
data1 = streams1[0]["time_series"].T
print(data1.shape)
assert data1.shape[0] == 4
data1[:4:2] -= data1[1:4:2]
data1 = data1[::2]
data1[:2] *= (1e-6 / 50 / 2)
sfreq = float(streams1[0]["info"]["nominal_srate"][0])
info = mne.create_info(2, sfreq, ["eeg", "stim"])
raw = mne.io.RawArray(data1, info)
raw.plot(scalings=dict(eeg=100e-6), duration=300, start=0)

fname=op.join(misc.data_path(), 'xdf', 'Avec_tête.xdf')

streams, header = pyxdf.load_xdf(r'C:\Users\Myriam\Documents\CurrentStudy\sub-P001\ses-S002\eeg\Avec_tête.xdf')
data = streams[0]["time_series"].T
print(data.shape)
assert data.shape[0] == 3
data[:4:2] -= data[1:4:2]
data = data[::2]
data[:2] *= (1e-6 / 50 / 2)
sfreq = float(streams[0]["info"]["nominal_srate"][0])
info = mne.create_info(2, sfreq, ["eeg", "stim"])
raw = mne.io.RawArray(data, info)
raw.plot(scalings=dict(eeg=100e-6), duration=300, start=0)


