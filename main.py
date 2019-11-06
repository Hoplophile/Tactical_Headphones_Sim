import numpy as np
from scipy import signal
from wav_handler import get_signal_from_file
from filters import *
from plotting import *
from scipy.fftpack import fft


path_to_wav = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/wavs/M4A1.wav'
path_to_wav2 = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/wavs/beretta_m9.wav'
path_to_wav3 = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/wavs/AK47.wav'
path_to_wav4 = 'C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/wavs/mossberg_500.wav'
order = 1
cutoff = 10000      # desired cutoff frequency of the filter, Hz
sr = 512000.0       # sample rate in Hz


def gen_sine():
    rate = sr
    freq = 100
    x = np.arange(80000)

    sinus = np.sin(2 * np.pi * freq * x / rate)
    return sinus, x


def main():
    # Get signal from .wav file
    wav_signal, wav_time = get_signal_from_file(path_to_wav)
    wav2_signal, wav2_time = get_signal_from_file(path_to_wav2)
    wav3_signal, wav3_time = get_signal_from_file(path_to_wav3)
    wav4_signal, wav4_time = get_signal_from_file(path_to_wav4)
    sin_signal, sin_time = gen_sine()

    # Filter the data
    wav_filtered = butter_lowpass_filter(wav_signal, cutoff, sr, order)
    wav2_filtered = butter_lowpass_filter(wav2_signal, cutoff, sr, order)
    wav3_filtered = butter_lowpass_filter(wav3_signal, cutoff, sr, order)
    wav4_filtered = butter_lowpass_filter(wav4_signal, cutoff, sr, order)

    # Fourier transform
    fourier_signal = fft(wav_filtered)
    # fourier_signal = fourier_signal[:len(fourier_signal)//2]
    fourier_x = np.linspace(0.0, stop=sr, num=len(fourier_signal))
    fourier_x = fourier_x[:len(fourier_signal)]

    fourier_signal2 = fft(wav2_filtered)
    fourier_signal2 = fourier_signal2[:len(fourier_signal2)//2]
    fourier_x2 = np.linspace(0.0, sr/2, len(fourier_signal2))

    fourier_signal3 = fft(wav3_filtered)
    fourier_signal3 = fourier_signal3[:len(fourier_signal3)//2]
    fourier_x3 = np.linspace(0.0, sr/2, len(fourier_signal3))

    fourier_signal4 = fft(wav4_filtered)
    fourier_signal4 = fourier_signal4[:len(fourier_signal4)//2]
    fourier_x4 = np.linspace(0.0, sr/2, len(fourier_signal4))

    fourier_signal_sin = fft(sin_signal)
    fourier_signal_sin = fourier_signal_sin[:len(fourier_signal_sin)//2]
    fourier_x_sin = np.linspace(0.0, sr/2, len(fourier_signal_sin))

    # Plot all orig+filtered
    plot_four_with_filt_sep(wav_signal, wav_filtered, wav_time, 'M4A1',
                            wav2_signal, wav2_filtered, wav2_time, 'Beretta M9',
                            wav3_signal, wav3_filtered, wav3_time, 'AK47',
                            wav4_signal, wav4_filtered, wav4_time, 'Mossberg 500')

    # Plot M4 with fft
    plot_orig_filt_fft(wav_signal, 'M4A1', wav_time,                                # original
                       wav_filtered, 'filtered M4A1', wav_time,                     # filtered
                       np.abs(fourier_signal), 'FFT of filtered M4A1', fourier_x)   # fft

    # Plot M9 with fft
    plot_orig_filt_fft(wav2_signal, 'Beretta', wav2_time,                                # original
                       wav2_filtered, 'filtered Beretta', wav2_time,                     # filtered
                       np.abs(fourier_signal2), 'FFT of filtered Beretta', fourier_x2)   # fft

    # Plot AK47 with fft
    plot_orig_filt_fft(wav3_signal, 'AK47', wav3_time,                                # original
                       wav3_filtered, 'filtered AK47', wav3_time,                     # filtered
                       np.abs(fourier_signal3), 'FFT of filtered AK47', fourier_x3)   # fft

    # Plot Mossberg with fft
    plot_orig_filt_fft(wav4_signal, 'Mossberg', wav4_time,                                # original
                       wav4_filtered, 'filtered Mossberg', wav4_time,                     # filtered
                       np.abs(fourier_signal4), 'FFT of filtered Mossberg', fourier_x4)   # fft

    plt.show()


if __name__ == '__main__':
    main()
