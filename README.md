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

`phase unwrapping` 

https://www.surina.net/article/time-and-pitch-scaling.html
