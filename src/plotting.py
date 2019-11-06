import matplotlib.pyplot as plt
import numpy as np


def plot_two_sep(first, caption_first, first_t, second, caption_second, second_t):

    plt.figure(figsize=(17, 8))
    plt.xlabel('Time [sec]')
    plt.subplot(2, 1, 1)
    plt.plot(first_t, first, 'b-', linewidth=0.5, label=caption_first)
    plt.legend()
    plt.xlim(right=0.15, left=-0.01)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.plot(second_t, second, 'g-', linewidth=0.5, label=caption_second, scalex=0.1)
    plt.legend()
    plt.xlim(right=20000, left=-0.01)
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    plt.show()


def plot_orig_filt_fft(orig, orig_txt, orig_t, filt, filt_txt, filt_t, fft, fft_txt, fft_t):
    plt.figure(figsize=(17, 8))
    plt.subplot(2, 1, 1)
    plt.plot(orig_t, orig, 'b-', linewidth=0.5, label=orig_txt)
    plt.plot(filt_t, filt, 'r-', linewidth=2, label=filt_txt)
    plt.xlabel('Time [sec]')
    plt.legend()
    # plt.xlim(right=0.2, left=-0.01)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.plot(fft_t, fft, 'g-', linewidth=1.5, label=fft_txt)
    plt.xlabel('Frequency [Hz]')
    plt.legend()
    plt.xlim(right=20000, left=-0.01)
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    # plt.show()


def plot_four_with_filt_sep(sig1, filt1, time1, name1,
                            sig2, filt2, time2, name2,
                            sig3, filt3, time3, name3,
                            sig4, filt4, time4, name4):
    plt.figure(figsize=(17, 8))
    plt.subplot(2, 2, 1)
    plt.plot(time1, sig1, 'b-', linewidth=0.5, label=name1)
    plt.plot(time1, filt1, 'r-', linewidth=2, label=(name1 + ' filtered'))
    plt.xlabel('Time [sec]')
    plt.legend()
    # plt.xlim(right=0.15, left=-0.01)
    plt.grid()
    plt.subplot(2, 2, 2)
    plt.plot(time2, sig2, 'b-', linewidth=0.5, label=name2)
    plt.plot(time2, filt2, 'r-', linewidth=2, label=(name2 + ' filtered'))
    plt.xlabel('Time [sec]')
    plt.legend()
    # plt.xlim(right=0.15, left=-0.01)
    plt.grid()
    plt.subplot(2, 2, 3)
    plt.plot(time3, sig3, 'b-', linewidth=0.5, label=name3)
    plt.plot(time3, filt3, 'r-', linewidth=2, label=(name3 + ' filtered'))
    plt.xlabel('Time [sec]')
    plt.legend()
    # plt.xlim(right=0.15, left=-0.01)
    plt.grid()
    plt.subplot(2, 2, 4)
    plt.plot(time4, sig4, 'b-', linewidth=0.5, label=name4)
    plt.plot(time4, filt4, 'r-', linewidth=2, label=(name4 + ' filtered'))
    plt.xlabel('Time [sec]')
    plt.legend()
    # plt.xlim(right=0.15, left=-0.01)
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    # plt.show()


def plot_two_on_one(first, caption_first, first_t, second, caption_second, second_t):

    plt.figure(figsize=(17, 8))
    plt.xlabel('Time [sec]')
    plt.plot(first_t, first, 'b-', linewidth=0.5, label=caption_first)
    plt.plot(second_t, second, 'r-', linewidth=1.5, label=caption_second)
    plt.legend()
    # plt.xlim(right=0.2, left=-0.01)
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    plt.show()


def plot_one(data, caption, time):
    plt.figure(figsize=(17, 8))
    plt.xlabel('Time [sec]')
    plt.plot(time, data, 'g-', linewidth=0.5, label=caption, scalex=0.1)
    plt.legend()
    # plt.xlim(right=0.2)
    plt.grid()

    plt.show()
