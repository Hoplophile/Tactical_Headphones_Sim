import numpy as np
from scipy import signal
from wav_handler import get_signal_from_file
from filters import *
from plotting import *
from scipy.fftpack import fft


path_to_wav = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/gunfire.wav'
path_to_wav2 = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/gunfire2.wav'
order = 5
cutoff = 10000      # desired cutoff frequency of the filter, Hz
sr = 705000.0       # sample rate, Hz


def gen_sine():
    rate = sr
    freq = 800
    x = np.arange(80000)

    sinus = np.sin(2 * np.pi * freq * x / rate)
    return sinus, x


def main():
    # Get signal from .wav file
    wav_signal, wav_time = get_signal_from_file(path_to_wav)
    wav2_signal, wav2_time = get_signal_from_file(path_to_wav2)
    sin_signal, sin_time = gen_sine()

    # wav_signal = wav_signal[len(wav_signal)//5:]
    # wav_time = wav_time[len(wav_time)//5:]

    # Filter the data
    wav_filtered = butter_lowpass_filter(wav_signal, cutoff, sr, order)
    wav2_filtered = butter_lowpass_filter(wav2_signal, cutoff, sr, order)
    sin_filtered = butter_highpass_filter(sin_signal, cutoff, sr, order)

    # Fourier transform
    fourier = fft(np.abs(wav_filtered))

    # Plot data
    # plot_two_sep(wav_signal, 'original', wav_time, wav_filtered, 'filtered', wav_time)
    # plot_one(wav_filtered, 'filtered', wav_time)
    plot_two_sep(wav_filtered, 'original', wav_time,
                 np.abs(fourier[:len(fourier)//100]), 'fourier', np.linspace(0.0, sr, 20912//100))
    # plot_one(np.abs(fourier[:len(fourier)//100]), 'fourier', np.linspace(0.0, sr, 20912//100))
    # plot_one(wav_filtered, 'sinus', wav_time)


if __name__ == '__main__':
    main()
