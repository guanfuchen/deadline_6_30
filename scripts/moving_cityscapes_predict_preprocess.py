#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np
import scipy.misc as misc
import glob

import utils
import cv2

if __name__ == '__main__':
    CityscapesRoot = os.path.expanduser('~/Data/cityscapes_enet_pred')
    CityscapesRootTrainAnnot = os.path.join(CityscapesRoot, '*')
    CityscapesRootTrainAnnotList = glob.glob(CityscapesRootTrainAnnot)
    MovingObjSavePath = '/tmp/trainannot_moving/'
    if not os.path.isdir(MovingObjSavePath):
        os.mkdir(MovingObjSavePath)
    for CityscapesRootTrainAnnotItem in CityscapesRootTrainAnnotList:
        #print(CityscapesRootTrainAnnotItem)
        CityscapesRootTrainAnnotItemFullPath = glob.glob(os.path.join(CityscapesRootTrainAnnotItem, '*'))
        CityscapesRootTrainAnnotItemFullPath.sort()
        for CityscapesRootTrainAnnotItemFullPathItem in CityscapesRootTrainAnnotItemFullPath:
            #print(CityscapesRootTrainAnnotItemFullPathItem)
            cityscapes_child_root_item_name = CityscapesRootTrainAnnotItem[CityscapesRootTrainAnnotItem.rfind('/')+1:]
            img_name = CityscapesRootTrainAnnotItemFullPathItem[CityscapesRootTrainAnnotItemFullPathItem.rfind('/')+1:]
            img = cv2.imread(CityscapesRootTrainAnnotItemFullPathItem, -1)
            height, width = img.shape
            mask_img_moving_mask = np.in1d(img, [11, 12, 13, 14, 15, 16, 17, 18]).reshape(height, width)
            img_moving = mask_img_moving_mask * img
            #print(cityscapes_child_root_item_name)
            #print(img_name)
            img_save_path = os.path.join(MovingObjSavePath, cityscapes_child_root_item_name)
            if not os.path.isdir(img_save_path):
                os.mkdir(img_save_path)
            img_save_path_file_name = os.path.join(img_save_path, img_name)
           #  print(np.unique(img))
            # cv2.imshow('img', img)
            # cv2.imshow('img_moving', img_moving)
            # cv2.waitKey(0)
            cv2.imwrite(img_save_path_file_name, img_moving)
            #break
        #break

