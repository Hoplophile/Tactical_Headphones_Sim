import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import wave


def butter_lowpass(cutoff, freq, order=5):
    nyq = 0.5 * freq
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, freq, order=5):
    b, a = butter_lowpass(cutoff, freq, order=order)
    y = lfilter(b, a, data)
    return y


# Filter requirements.
order = 6
sr = 705000.0       # sample rate, Hz
cutoff = 100  # desired cutoff frequency of the filter, Hz


spf = wave.open('C:/Users/zj6pz3/PycharmProjects/Tactical_headphones/gunfire.wav', 'r')

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, dtype=int)

# Get only one channel
mono = []
for index, datum in enumerate(signal):
    if index % 2:
        mono.append(datum)

# Get time from indices
fs = spf.getframerate()
Time = np.linspace(0, len(signal)/2/fs, num=len(signal)/2)

#Plot
# plt.figure(1)
# plt.title('Signal Wave...')
# plt.plot(Time, mono)
# plt.show()
T = 1/sr
N = len(mono)



b, a = butter_lowpass(cutoff, sr, order)

w, h = freqz(b, a, worN=8000)
# plt.subplot(2, 1, 1)
# plt.plot(0.5*sr*w/np.pi, np.abs(h), 'b')
# plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
# plt.axvline(cutoff, color='k')
# plt.xlim(0, 0.5*fs)
# plt.title("Lowpass Filter Frequency Response")
# plt.xlabel('Frequency [Hz]')
# plt.grid()
# plt.show()


xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Filter the data, and plot both the original and filtered signals.
filtered = butter_lowpass_filter(mono, cutoff, sr, order)

plt.subplot(2, 1, 2)
plt.plot(Time, mono, 'b-', label='data')
plt.plot(xf, mono, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()



#
#
# yf = np.fft.fft(mono)
# xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#
# fig, (ax1, ax2) = plt.subplots(1, 2)
# ax1.plot(xf, 2.0/N * np.abs(yf[:N//2]))
# ax2.plot(Time, mono)
# plt.show()
