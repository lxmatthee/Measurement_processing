import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter, freqz, blackmanharris
import pandas as pd


def calc_freq(df, signal_prop, plot=False):
    """
    Calculate the frequency of a signal from a DataFrame.
    Parameters:
        - df: pandas.DataFrame containing the signal
        - signal_prop: dictionary with signal properties (grid, sample_rate, duration_s)
        - plot: boolean indicating whether to plot the frequency over time
    Returns:
        - freq: list containing the calculated frequency values
    """
    freq = []
    last_point = df['grid'][0]
    debounce = -1
    marker = []
    calc_freq = None
    zero_cross_flag = False
    for i, data_point in enumerate(df['grid']):
        if data_point > 0 and last_point <= 0 and debounce < 0:
            debounce = 100
            marker.append(i)
            zero_cross_flag = True
        if data_point < 0 and last_point >= 0 and debounce < 0:
            debounce = 100
            marker.append(i)
            zero_cross_flag = True
        if zero_cross_flag and len(marker) > 2:
            calc_freq = 1 / ((i - marker[-2]) * (1 / signal_prop['sample_rate']) * 2)
            zero_cross_flag = False
        freq.append(calc_freq)
        zero_cross_flag = False
        last_point = data_point
        debounce -= 1

    if plot:
        # Create plot
        fig, ax = plt.subplots()
        ax.plot(df['time_ms'], freq, color="blue", label="freq", linewidth=2)

        # Set plot attributes
        ax.tick_params(axis='y', labelcolor="black", labelsize=10)
        ax.set_ylim((40, 60))
        ax.set_xlabel('Time (ms)', fontsize=10)
        ax.set_ylabel('Frequency', color="black", fontsize=10)
        ax.spines['left'].set_linewidth(2)
        ax.spines['bottom'].set_linewidth(1.5)
        ax.legend(loc='upper right')
        plt.show()

    return freq


def create_signal(signal_properties):
    """
    Create a sinusoidal signal from a given set of properties.
    Parameters:
        - signal_properties: dictionary containing the signal properties (grid, sample_rate, duration_s)
    Returns:
        - df: pandas.DataFrame containing the sinusoidal signal
    """
    # Set the sampling rate and duration of the signals
    sr = signal_properties['sample_rate']  # Samples per second
    dur = signal_properties['duration_s']  # Duration in seconds

    # Create time array
    time = np.arange(0, dur, 1/sr)
    # Scale time to ms for plot
    time_ms = time * 1000

    # Create sinusoidal signal
    sig = np.sin(2 * np.pi * signal_properties['grid'] * time)

    # Add the signal to a DataFrame
    df = pd.DataFrame({'grid': sig, "time_ms": time_ms})

    return df


if __name__ == '__main__':
    # Define signal properties
    signal_prop = {
        'grid': 50,  # Signal frequency in Hz
        'sample_rate': 10e4,  # Sampling rate in Hz
        'duration_s': 1  # Signal duration in seconds
    }

    # Create sinusoidal signal
    signal_df = create_signal(signal_prop)

    # Calculate frequency of the signal and
    # Plot grid voltage
    signal_df['freq'] = calc_freq(signal_df, signal_prop, plot=True)