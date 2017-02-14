#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def grab_data(working_file=None):

    data_file = working_file

    if not data_file:
        print("we need a data file to work with...")
        data_file = input("file to open: ")

    f = open(data_file, 'r')

    values = []
    average = []
    deviation = []

    for line in f:
        line = re.sub('[a-zA-Z:, ]', '', line)
        line = line.replace('\n','')
        line = line.replace('±', ' ')
        if len(line) > 0:
            values.append(line.split(' '))

    for epoch in values:
        average.append(epoch[0])
        deviation.append(epoch[1])

    epochs = range(len(average))

    # return structure is y, x, error (average, epochs, deviation)
    return average, epochs, deviation


