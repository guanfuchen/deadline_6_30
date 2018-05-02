#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np
import scipy.misc as misc
import selectivesearch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

if __name__ == '__main__':
    MovingObjSavePath = '/tmp/train_48x36/'
    if os.path.isdir(MovingObjSavePath):
        pass
    else:
        exit(0)

    moving_obj_data = []
    CamVidRootTrainAnnotList = os.listdir(MovingObjSavePath)
    CamVidRootTrainAnnotListLen = len(CamVidRootTrainAnnotList)
    timestamps = 20
    for CamVidRootTrainAnnotListIndex in range(CamVidRootTrainAnnotListLen-timestamps):
        # print(CamVidRootTrainAnnotListIndex)
        # 20 timestamps
        moving_obj_data_sample = []
        for timestamp in range(timestamps):
            img = misc.imread(os.path.join(MovingObjSavePath, CamVidRootTrainAnnotList[CamVidRootTrainAnnotListIndex+timestamp]), flatten=True)
            # print(img.shape)
            moving_obj_data_sample.append(img)
        moving_obj_data.append(moving_obj_data_sample)

    moving_obj_data = np.array(moving_obj_data)
    moving_obj_data = moving_obj_data.transpose((1, 0, 2, 3))
    print(moving_obj_data.shape)
    np.save('train_48x36.npy', moving_obj_data)
