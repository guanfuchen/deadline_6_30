#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np
import scipy.misc as misc
import selectivesearch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import utils

if __name__ == '__main__':
    MovingObjSavePath = '/tmp/trainannot_moving/'
    if os.path.isdir(MovingObjSavePath):
        pass
    else:
        exit(0)
    CamVidRootTrainAnnotList = os.listdir(MovingObjSavePath)
    for CamVidRootTrainAnnotItem in CamVidRootTrainAnnotList:
        print(CamVidRootTrainAnnotItem)
        CamVidRootTrainAnnotItemFullPath = os.path.join(MovingObjSavePath, CamVidRootTrainAnnotItem)
        img = misc.imread(CamVidRootTrainAnnotItemFullPath)
        height, width = img.shape
        img = utils.decode_segmap(img)
        img_lbl, regions = selectivesearch.selective_search(img, scale=500, sigma=0.9, min_size=10)

        candidates = set()
        for r in regions:
            if r['rect'] in candidates:
                pass
                continue
            if r['size'] < 2000:
                pass
                continue
            x, y, w, h = r['rect']
            if h == 0 or w == 0:
                continue
            elif w / h > 1.2 or h / w > 1.2:
                pass
                continue
            candidates.add(r['rect'])

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
        ax.imshow(img)
        for x, y, w, h in candidates:
            rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
            ax.add_patch(rect)
        plt.show()

