import numpy as np
import matplotlib.pyplot as plt

def center_of_gravity(x):
    '''
    Find the center of gravity of a vector, x.
    If x=[x0,x1,...,xn], then you should return
    c = ( 0*x0 + 1*x1 + 2*x2 + ... + n*xn ) / sum(x)
    where n = len(x)-1.
    
    Recommended method: use np.arange, np.dot, and np.sum.
    '''
    indices = np.arange(0, len(x))
    c = np.dot(indices, x) / np.sum(x)
    return c

def matched_identity(x):
    '''
    Create an identity matrix that has the same number of rows as x has elements.
    Hint: use len(x), and use np.eye.
    '''
    N = len(x)
    I = np.eye(N)
    # I = np.eye(len(x))
    return I

def sine_and_cosine(t_start, t_end, t_steps):
    '''
    Create a time axis, and compute its cosine and sine.
    Hint: use np.linspace, np.cos, and np.sin
    '''
    t = np.linspace(t_start, t_end, t_steps)
    x = np.cos(t)
    y = np.sin(t)
    return t, x, y
