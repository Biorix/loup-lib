# -*- coding: utf-8 -*-
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import time

def rescale(x, in_min, in_max, out_min, out_max):
    """
    Return rescaled data form a previous min and max to a new one
        e.g: in data is between -5 and +5 and you need 0-100
    @param x: data to rescale
    @type x: int|float|list|tuple
    @param in_min: initial minimum value
    @type in_min: int|float
    @param in_max: initial maximum value
    @type in_max: int|float
    @param out_min: final minimum value
    @type out_min: int|float
    @param out_max:final maximum value
    @type out_max: int|float
    @return: the data rescaled
    @rtype: float
    """
    try:
        return ((i - in_min) * (out_max - out_min) / (in_max - in_min) + out_min for i in x)
    except TypeError:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def chooseOpenFile():
    filepath = askopenfilename() # show an "Open" diaslog box and return the path to the selected file
    filename = filepath.split(r'/')[-1]
    return filepath, filename

def timestamp2sec(timestamp):
    t = time.strptime(timestamp, "%Y-%m-%d %H:%M")
    time_in_seconds = int(time.mktime(t))