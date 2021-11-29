from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
text = str("Але мені не подобається, що восени часто йдуть дощі? І вони змінюють наші плани з приводу прогулянки!!! Зате восени буває «бабине літо». Природа ніби хоче повернути літо назад. Яскраво світить сонце та навіть не віриться, що вже осінь")
def count_sign():
    symbols = ["—", "!", ".", ",", "?", "..."]
    for i in range(0, len(symbols)):
        xdata = [symbols[i]]
        ydata = [text.count(symbols[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_sign()
