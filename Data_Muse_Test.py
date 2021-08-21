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

fname1=op.join(misc.data_path(), 'xdf', 'Avec_tete.xdf')

streams1, header1 = pyxdf.load_xdf(r'C:\Users\Myriam\Documents\CurrentStudy\sub-P001\ses-S001\eeg\Avec_tete.xdf')
data1 = streams1[0]["time_series"].T
print(data1.shape)
assert data1.shape[0] == 4
data1 *= (1e-6 / 50 / 2)
channels = ["TP9", "AF7", "AF8", "TP10"]
info1 = mne.create_info(channels, 256, ch_types="eeg")
raw1 = mne.io.RawArray(data1, info1)
print("raw1.info", raw1.info)
figS = mne.viz.plot_raw(raw1, duration=1, start=60, title="Avec_tête")
psdS = mne.viz.plot_raw_psd(raw1, fmin=0, fmax=128, picks="all", show=True)

fname=op.join(misc.data_path(), 'xdf', 'Sans_tete.xdf')

streams, header = pyxdf.load_xdf(r'C:\Users\Myriam\Documents\CurrentStudy\sub-P002\ses-S001\eeg\Sans_tete.xdf')
data = streams[0]["time_series"].T
print(data.shape)
assert data.shape[0] == 4
data *= (1e-6 / 50 / 2)
channels = ["TP9", "AF7", "AF8", "TP10"]
info = mne.create_info(channels, 256, ch_types="eeg")
raw = mne.io.RawArray(data, info)
print("raw1.info", raw.info)
figA = mne.viz.plot_raw(raw, duration=1, start=60, title="Sans-tête")
psdA = mne.viz.plot_raw_psd(raw, fmin=0, fmax=128, picks="all", show=True)



