import sounddevice as sd
import numpy as np
import math

# static class, use to get microphone decibel
class Microphone():
    duration = 0.08 # duration of echantillonage.
    sampleRate = 44100 # hard coded value to get song.

    durationRate = int(duration * sampleRate) # duration mult for use.

    decibel = 0 # output decibel.

    #def __init__(self):
    #    pass


    @staticmethod
    async def updateDecibel():

        print("T")



        #audioData = sd.rec(
        #    durationRate, 
        #    samplerate=sample_rate, 
        #    channels=1, 
        #    dtype='float64'
        #)
        #sd.wait()

        ## root mean square.
        #rms = np.sqrt(np.mean(audioData**2))

        #if rms <= 0:
        #    Microphone.decibel = 0 # -float('inf')
        #    return

        #Microphone.decibel = 20 * math.log10(rms)
        



