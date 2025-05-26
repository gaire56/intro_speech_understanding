import numpy as np

def minimum_Fs(f):
    '''
    Find the lowest sampling frequency that would avoid aliasing for a pure tone at f Hz.
    According to the Nyquist theorem, the minimum Fs must be greater than 2*f.
    '''
    Fs = 2 * f
    return Fs

def omega(f, Fs):
    '''
    Find the radial frequency (omega) that matches a given f and Fs.
    omega = 2 * pi * f / Fs
    '''
    omega = 2 * np.pi * f / Fs
    return omega

def pure_tone(omega, N):
    '''
    Create a pure tone of N samples at omega radians/sample.
    The signal is defined as cos(omega * n) for n = 0 to N-1
    '''
    n = np.arange(N)
    x = np.cos(omega * n)
    return x
