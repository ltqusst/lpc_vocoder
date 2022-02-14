# lpc_vocoder
Simple LPC vocoder in Python

## Formants & Vocoder
https://www.youtube.com/watch?v=jpbFnsusfp0
https://en.wikipedia.org/wiki/PSOLA
https://dsp.stackexchange.com/questions/28526/how-does-formant-shifting-work


## PSOLA

> F. Charpentier and M. Stella. "Diphone synthesis using an overlap-add technique for speech waveforms concatenation." In Int. Conf. Acoustics, Speech, and Signal Processing (ICASSP). Vol. 11. IEEE, 1986.

It's base on STFT+OLA framework, and achieves pitch/formants shifting by frequency domain manipulation, it extracts `spectral envelop`(containing the formants information) from STFT result and recover `source component`(contains pitch information) by dividing STFT spectrum by `spectral envelop`. then these two signals can be separately manipulated (by interpolation based shifting) and recombined before inverse DFT is applied.

The window's starting position is choosen to be `pitch-synchronous` so it contains waveforms of same/similar pitch.

## TD-PSOLA
https://github.com/sannawag/TD-PSOLA
https://courses.engr.illinois.edu/ece420/sp2022/lab5/lab/

The description is very detail, including principle and example.

Since it works on cycle by cycle basis, the limitation would be how to robustly estimate `h(t)` of each fundamental period of the signal. also it didn't handle consonant.

## Phase Vocoder for pitch shifting

J.L. Flanagan and R.M. Golden, '"Phase Vocoder, Bell yfl,g Tech. J., Vol. 45,
November 1966, pp. 1493—1509.
https://www.ee.columbia.edu/~dpwe/e6820/papers/FlanG66.pdf

Vocoder : voice encoder/decoder
Phase Vocoder : based on filter-banks framework, study how to encode voice signal as magnitude + phase for compression & transmission.
                magnitude and phase derivative is encoded with much lower rate 20~30Hz.

Short Term Spectral Analysis, Synthesis, and Modification by Discrete Fourier Transform
https://courses.engr.illinois.edu/ece420/sp2019/lab3/STFT.pdf

Use FFT/IFFT instead of convolution


M.R. Portnoff, "Time—Scale Modification of Speech Based on Short—Time Fourier Analysis",
IEEE Trans. Acouat., Speech Signal Processing, Vol. ASSP—29, No. 3, June
1981, pp. 374—390.

Seneff, '"System to Independently Modify Excitation and/or Spectrum of Speech Waveform Without Explicit Pitch Extrsction"
Trans. Acoust., Speech Signal Processing,
Vol. ASSP—30, No. 4, August 1982, pp.
566—578.

## Signal Estimation from Modified Short—Time Fourier Transform
D.W. Griffin and J.S. Lim, '"Signal Estimation from Modified Short—Time Fourier Transform"
IEEE Trans. Acoust., Speech Signal Processing, Vol. ASSP—32, No. 2, April
1984, pp. 236—243.

High Quality Time-Scale Modification for Speech
Salim Roucos and Alexander M. Wilgus
1985 IEEE

`phase unwrapping` 

https://www.surina.net/article/time-and-pitch-scaling.html

## Pitch detection

https://stackoverflow.com/questions/32595404/pitch-detection-in-python
https://pypi.org/project/crepe/
