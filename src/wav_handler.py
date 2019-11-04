import wave
import numpy as np
# from scipy import signal


def get_raw_from_file(path):
    spf = wave.open(path, 'r')
    raw_signal = spf.readframes(-1)
    raw_signal = np.frombuffer(raw_signal, dtype='int')
    time = np.linspace(0, len(raw_signal) / 2 / spf.getframerate(), num=len(raw_signal)//2)

    return raw_signal, time


def get_mono_from_signal(raw_signal):
    mono = []
    for index, datum in enumerate(raw_signal):
        if index % 2:
            mono.append(datum)

    return mono


def get_signal_from_file(path):
    raw, time = get_raw_from_file(path)
    return get_mono_from_signal(raw), time

