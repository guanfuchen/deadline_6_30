#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def decode_segmap(temp, plot=False):
    Sky = [128, 128, 128]
    Building = [128, 0, 0]
    Pole = [192, 192, 128]
    # Road_marking
    Road_marking = [255, 69, 0]
    Road = [128, 64, 128]
    Pavement = [60, 40, 222]
    Tree = [128, 128, 0]
    SignSymbol = [192, 128, 128]
    Fence = [64, 64, 128]
    Car = [64, 0, 128]
    Pedestrian = [64, 64, 0]
    Bicyclist = [0, 128, 192]
    Unlabelled = [0, 0, 0]

    label_colours = np.array([Sky, Building, Pole, Road, Pavement, Tree,
                              SignSymbol, Road_marking, Car,
                              Pedestrian, Fence, Unlabelled])

    height, width = temp.shape
    rgb = np.zeros((height, width, 3), dtype=np.uint8)

    for row in range(height):
        for col in range(width):
            label = temp[row, col]
            color = label_colours[label]
            #             if label==0:
            #                 print('label:', 0)
            rgb[row, col, :] = color

            #     rgb = rgb/255.0

    if plot:
        plt.imshow(rgb)
        plt.show()
    else:
        return rgb
