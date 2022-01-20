from typing import List
import numpy as np
import scipy, scipy.io, scipy.io.wavfile, scipy.signal
import IPython
import matplotlib.pyplot as plt
from vscode_audio import Audio

def play_sound(sound, rate=44100, name="", spectrum = 0, waveform = 1, figsize=(32,8)):
    """Play a mono 44Khz sound file in the browser"""
    #return IPython.display.display(IPython.display.Audio(sound,rate=rate))
    if waveform > 0 or spectrum >= 0:
        plt.figure(figsize=figsize, dpi= 100, facecolor='w', edgecolor='k')

        if (isinstance(sound, list)):
            N = len(sound)
            for i in range(N):
                plt.subplot(N, 1, i+1)
                times = np.arange(0, len(sound[i])/44100, 1/44100)
                plt.plot(times, sound[i], 'k-')
                plt.title(name)
            plt.show()
            return IPython.display.display(Audio(np.hstack(sound),sr=rate, name=name))

        if waveform > 0:
            plt.subplot(211)
            times = np.arange(0, len(sound)/44100, 1/44100)
            plt.plot(times, sound, 'k-')
            plt.xlabel("Time (s)")
            plt.ylabel("sample")

        if spectrum == 1:
            plt.subplot(212)
            powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(sound, NFFT=1024, Fs=rate, scale='dB')
            plt.xlabel('Time')
            plt.ylabel('Frequency')

        if spectrum == 0:
            fourier_transform = np.fft.rfft(sound)
            power_spectrum = 20 * np.log10(np.abs(fourier_transform))
            frequency = np.linspace(0, rate/2, len(power_spectrum))
            plt.subplot(212)
            plt.plot(frequency, power_spectrum)
            plt.xlim(0,4000)
            plt.ylim(bottom=0)
            plt.xlabel('Frequency')
            plt.ylabel('power(dB)')

        plt.title(name)
        plt.show()
    return IPython.display.display(Audio(sound,sr=rate, name=name))

def load_wave(fname):
    """Load a 16 bit wave file and return normalised in 0,1 range"""
    # load and return a wave file
    sr, wave = scipy.io.wavfile.read(fname)
    return wave/32768.0
