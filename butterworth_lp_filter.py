
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter, freqz, blackmanharris
import pandas as pd



def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def filter(data, n, order, fs, cut_off):
    #@params
    # data    : Signal to be filtered
    # n       : Signal length in data points
    # order   : Order of the filter
    # fs      : Signal sample rate
    # cut_off : Filter cut off frequency fc
    # @Returns: Filtered signal - List   
  
    # Get the filter coefficients so we can check its frequency response. Optional
    """ 
    b, a = butter_lowpass(cut_off, fs, order)
    # Plot the frequency response.
    w, h = freqz(b, a, worN=8000)
    t = np.linspace(0, n , n, endpoint=False) 
    """

    # Filter the data, and plot both the original and filtered signals.
    y = butter_lowpass_filter(data, cut_off, fs, order)
    return y

def create_signal(signal_properties, plot=False):
    # Set the sampling rate and duration of the signals
    sr = signal_properties['sample_rate'] # Samples per second
    dur = signal_properties['duration_s'] # Duration in seconds

    # Create time array
    time = np.arange(0, dur, 1/sr)
    # Scale time to ms for plot
    time_df = time * 1000

    # Create f1 Hz and f2 Hz signals
    sig_f1 = np.sin(2 * np.pi * signal_properties['f1'] * time)
    sig_f2 = np.sin(2 * np.pi * signal_properties['f2'] * time)
    
    # Combine the signals
    sig_mixed = sig_f1 + sig_f2

    # Add the signals to a DataFrame
    df = pd.DataFrame({'f1': sig_f1, 'f2': sig_f2, 'sig_mixed': sig_mixed, "time_ms": time_df})

    if plot:
      df.plot(y=['f1', 'f2', 'sig_mixed'])
      plt.show()
    return df

if __name__ == '__main__':
    
    # Signal f1, f2 freq in Hz, sample rate and duration in seconds
    signal_prop = {
                    'f1': 50, 
                    'f2': 1000, 
                    'sample_rate': 10e4, 
                    'duration_s': 1
                  }
    
    # Filter cut off frequency in Hz
    filter_cut_off = 100
    
    # Create signal
    df = create_signal(signal_prop, plot=False)

    # Ontain filtered signal
    df['filtered'] = filter(df['sig_mixed'], len(df['sig_mixed']), 5, signal_prop['sample_rate'], filter_cut_off)

    # Plot mixed signal and filtered signal
    ax1 = df.plot(y=['sig_mixed', 'filtered'], x='time_ms')
    ax1.set_xlabel('Time (ms)', fontsize=10)
    ax1.set_ylabel('Signal Amplitude |A|', color="black", fontsize=10)
    ax1.tick_params(axis='y', labelcolor="black", labelsize=10)
    ax1.spines['left'].set_linewidth(2)
    ax1.spines['bottom'].set_linewidth(1.5)
    plt.show()


    

 