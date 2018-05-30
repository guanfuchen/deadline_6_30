#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np
import scipy.misc as misc
import selectivesearch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

if __name__ == '__main__':
    MovingObjSavePath = os.path.expanduser('~/Data/cityscapes_enet_pred_trainannot_moving_128x64/stuttgart_00')
    if os.path.isdir(MovingObjSavePath):
        pass
    else:
        exit(0)

    moving_obj_data = []
    CityscapesRootTrainAnnotList = os.listdir(MovingObjSavePath)
    CityscapesRootTrainAnnotListLen = len(CityscapesRootTrainAnnotList)
    # CityscapesRootTrainAnnotListLen = min(CityscapesRootTrainAnnotListLen, 50)
    timestamps = 20
    for CityscapesRootTrainAnnotListIndex in range(CityscapesRootTrainAnnotListLen-timestamps):
        # print(CityscapesRootTrainAnnotListIndex)
        # 20 timestamps
        moving_obj_data_sample = []
        for timestamp in range(timestamps):
            img = misc.imread(os.path.join(MovingObjSavePath, CityscapesRootTrainAnnotList[CityscapesRootTrainAnnotListIndex+timestamp]), flatten=True)
            # print(img.shape)
            moving_obj_data_sample.append(img)
        moving_obj_data.append(moving_obj_data_sample)

    moving_obj_data = np.array(moving_obj_data)
    moving_obj_data = moving_obj_data.transpose((1, 0, 2, 3))
    print(moving_obj_data.shape)
    np.save('train_cityscapes_128x64.npy', moving_obj_data)
