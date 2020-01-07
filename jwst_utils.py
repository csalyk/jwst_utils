import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.constants import c
import pdb as pdb
import matplotlib as matplotlib

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


def make_miri_mrs_figure():
    x_1a=np.linspace(4.87,5.82,num=50)
    y_1a = [get_miri_mrs_resolution('1A',myx) for myx in x_1a]
    
    x_1b=np.linspace(5.62,6.73,num=50)
    y_1b = [get_miri_mrs_resolution('1B',myx) for myx in x_1b]
    
    x_1c=np.linspace(6.49,7.76,num=50)
    y_1c = [get_miri_mrs_resolution('1C',myx) for myx in x_1c]
    
    x_2a=np.linspace(7.45,8.90,num=50)
    y_2a = [get_miri_mrs_resolution('2A',myx) for myx in x_2a]
    
    x_2b=np.linspace(8.61,10.28,num=50)
    y_2b = [get_miri_mrs_resolution('2B',myx) for myx in x_2b]
    
    x_2c=np.linspace(9.91,11.87,num=50)
    y_2c = [get_miri_mrs_resolution('2C',myx) for myx in x_2c]
    
    x_3a=np.linspace(11.47,13.67,num=50)
    y_3a = [get_miri_mrs_resolution('3A',myx) for myx in x_3a]
    
    x_3b=np.linspace(13.25,15.80,num=50)
    y_3b = [get_miri_mrs_resolution('3B',myx) for myx in x_3b]
    
    x_3c=np.linspace(15.30,18.24,num=50)
    y_3c = [get_miri_mrs_resolution('3C',myx) for myx in x_3c]
    
    x_4a=np.linspace(17.54,21.10,num=50)
    y_4a = [get_miri_mrs_resolution('4A',myx) for myx in x_4a]
    
    x_4b=np.linspace(20.44,24.72,num=50)
    y_4b = [get_miri_mrs_resolution('4B',myx) for myx in x_4b]
    
    x_4c=np.linspace(23.84,28.82,num=50)
    y_4c = [get_miri_mrs_resolution('4C',myx) for myx in x_4c]
    
    fig=plt.figure()
    ax1=fig.add_subplot(111)
    ax1.plot(x_1a,y_1a,label='1A')
    ax1.plot(x_1b,y_1b,label='1B')
    ax1.plot(x_1c,y_1c,label='1C')
    ax1.plot(x_2a,y_2a,label='2A')
    ax1.plot(x_2b,y_2b,label='2B')
    ax1.plot(x_2c,y_2c,label='2C')
    ax1.plot(x_3a,y_3a,label='3A')
    ax1.plot(x_3b,y_3b,label='3B')
    ax1.plot(x_3c,y_3c,label='3C')
    ax1.plot(x_4a,y_4a,label='4A')
    ax1.plot(x_4b,y_4b,label='4B')
    ax1.plot(x_4c,y_4c,label='4C')
    
    ax1.legend()
    ax1.set_xlim(4.5,45.1)
    ax1.set_ylim(500,4500)
    ax1.set_xscale('log')
    ax1.set_xticks([5,6,7,8,9,10,20])
    ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax1.set_xlabel('Wavelength [$\mu$m]',fontsize=18)
    ax1.set_ylabel('Resolution (R)',fontsize=18)
    plt.show()
    return
