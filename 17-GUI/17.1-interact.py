# it works only in jypinter notebook
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

interact(func, x = 10)
