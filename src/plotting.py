import matplotlib.pyplot as plt
import numpy as np


def plot_two_sep(first, caption_first, first_t, second, caption_second, second_t):

    plt.figure(figsize=(17, 8))
    plt.xlabel('Time [sec]')
    plt.subplot(2, 1, 1)
    plt.plot(first_t, first, 'b-', linewidth=0.5, label=caption_first)
    plt.legend()
    plt.xlim(right=0.3, left=-0.01)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.plot(second_t, second, 'g-', linewidth=0.5, label=caption_second, scalex=0.1)
    plt.legend()
    plt.xlim(right=20000, left=-0.01)
    plt.grid()

    plt.subplots_adjust(hspace=0.35)
    plt.show()


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
