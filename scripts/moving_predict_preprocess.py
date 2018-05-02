#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np
import scipy.misc as misc

import utils

if __name__ == '__main__':
    CamVidRoot = os.path.expanduser('~/Data/CamVid/')
    CamVidRootTrainAnnot = os.path.join(CamVidRoot, 'trainannot')
    CamVidRootTrainAnnotList = os.listdir(CamVidRootTrainAnnot)
    MovingObjSavePath = '/tmp/trainannot_moving/'
    if not os.path.isdir(MovingObjSavePath):
        os.mkdir(MovingObjSavePath)
    for CamVidRootTrainAnnotItem in CamVidRootTrainAnnotList:
        print(CamVidRootTrainAnnotItem)
        CamVidRootTrainAnnotItemFullPath = os.path.join(CamVidRootTrainAnnot, CamVidRootTrainAnnotItem)
        img = misc.imread(CamVidRootTrainAnnotItemFullPath)
        # img_moving = np.copy(img)
        height, width = img.shape
        # for row in range(height):
        #     for col in range(width):
        #         img_value = img_moving[row, col]
        #         if img_value == 8 or img_value == 9:
        #             pass
        #         else:
        #             img_moving[row, col] = 11
        mask_img_moving_mask = np.in1d(img, [8, 9]).reshape(height, width)
        img_moving = mask_img_moving_mask * img

        misc.imsave(os.path.join(MovingObjSavePath, CamVidRootTrainAnnotItem), img_moving)
