# Measurement_processing
Functions for processing electrical grid measurements

README

This script is designed to calculate and plot the frequency of a sine wave signal. The script takes in the signal properties such as the frequency of the signal, the sampling rate, and the duration of the signal in seconds. The script creates a sine wave signal based on the input signal properties and calculates the frequency of the signal.

The script uses the following external libraries:

NumPy
Matplotlib
SciPy
Pandas
The script contains the following functions:

create_signal(signal_properties): This function takes in the signal properties and creates a sine wave signal based on the input signal properties. The function returns a Pandas DataFrame containing the signal data.
calc_freq(data_Frame, signal_prop, plot=False): This function takes in the signal data frame and signal properties and calculates the frequency of the signal. The function also has an optional plot parameter that, when set to True, plots the frequency of the signal over time using Matplotlib.
main(): This function is the main entry point of the script. It creates a sine wave signal based on the input signal properties, calculates the frequency of the signal, and plots the frequency of the signal over time.
To run the script, simply execute the script file. The script will create a sine wave signal based on the input signal properties and plot the frequency of the signal over time.

The script can be customized by modifying the input signal properties. The script can also be modified to perform additional signal processing tasks such as filtering or Fourier transforms.

Contributing
If you would like to contribute to the development of this script, please open an issue or pull request on the GitHub repository.
