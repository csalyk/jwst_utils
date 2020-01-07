import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.constants import c
import pdb as pdb

def get_miri_mrs_resolution(subband, wavelength):
    '''
    Retrieve approximate MIRI MRS spectral resolution given a wavelength
 
    Parameters
    
    ---------
    subband: string
      Subband (1A, 1B, ...4C)

    wavelength: float
      Wavelength in microns

    Returns

    ---------
    R: float
      Spectral resolution

    '''

    #Define spectral resolution dictionaries.  Table 1 of Wells et al. MIRI paper
    w0={
        "1A":4.87,
        "1B":5.62,
        "1C":6.49,
        "2A":7.45,
        "2B":8.61,
        "2C":9.91,
        "3A":11.47,
        "3B":13.25,
        "3C":15.30,
        "4A":17.54,
        "4B":20.44,
        "4C":23.84
        }
    w1={
        "1A":5.82,
        "1B":6.73,
        "1C":7.76,
        "2A":8.90,
        "2B":10.28,
        "2C":11.87,
        "3A":13.67,
        "3B":15.80,
        "3C":18.24,
        "4A":21.10,
        "4B":24.72,
        "4C":28.82
        }     
    R0={
        "1A":3320.,
        "1B":3190.,
        "1C":3100.,
        "2A":2990.,
        "2B":2750.,
        "2C":2860.,
        "3A":2530.,
        "3B":1790.,
        "3C":1980.,
        "4A":1460.,
        "4B":1680.,
        "4C":1630.
        }
    R1={
        "1A":3710.,
        "1B":3750.,
        "1C":3610.,
        "2A":3110.,
        "2B":3170.,
        "2C":3300.,
        "3A":2880.,
        "3B":2640.,
        "3C":2790.,
        "4A":1930.,
        "4B":1770.,
        "4C":1330.
        }    
    
    m=(R1[subband]-R0[subband])/(w1[subband]-w0[subband])
    y0=R0[subband]
    x0=w0[subband]
    R=y0+m*(wavelength-x0)
    return R

def get_miri_mrs_wavelengths(subband):
    w0={
        "1A":4.87,
        "1B":5.62,
        "1C":6.49,
        "2A":7.45,
        "2B":8.61,
        "2C":9.91,
        "3A":11.47,
        "3B":13.25,
        "3C":15.30,
        "4A":17.54,
        "4B":20.44,
        "4C":23.84
        }
    w1={
        "1A":5.82,
        "1B":6.73,
        "1C":7.76,
        "2A":8.90,
        "2B":10.28,
        "2C":11.87,
        "3A":13.67,
        "3B":15.80,
        "3C":18.24,
        "4A":21.10,
        "4B":24.72,
        "4C":28.82
        }
    return (w0[subband],w1[subband])
