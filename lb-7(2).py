from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
text = str("In Kiev, on November 27, 549 cases of coronavirus infection were confirmed, 31 people died from Covid-19 this Saturday, and 281 people recovered.")
def count_letters():
    alphabet = ["a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y",
                "z"]
    for i in range(0, len(alphabet)):
        xdata = [alphabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_letters()