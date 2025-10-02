import sounddevice as sd
import numpy as np
import math
import asyncio

# static class, use to get microphone decibel
class Microphone():
    duration = 0.03 # duration of echantillonage.
    sampleRate = 44100 # hard coded value to get song.

    durationRate = int(duration * sampleRate) # duration mult for use.

    decibel = 0 # output decibel.

    tresholdTalk = 60 # ref decibel used for unable mouth when talk.


    @staticmethod
    async def updateDecibel(): #async 

        audioData = sd.rec(
            Microphone.durationRate, 
            samplerate=Microphone.sampleRate, 
            channels=1, 
            dtype='float64'
        )

        # wait end of echantillon.
        sd.wait()

        # root mean square.
        rms = np.sqrt(np.mean(audioData**2))

        # get decibel current echantillon.
        currentDecibel = 0
        if rms > 0:
            currentDecibel = int(20 * math.log10(rms))
            currentDecibel += 100
            #print(f"cd : {currentDecibel}")
            # current decibel is between 30 and 50, 100 (with mic).

        # apply decibel current, with lissage.
        Microphone.decibel = int(Microphone.decibel * 0.85)
        Microphone.decibel -= 35
        Microphone.decibel += currentDecibel
        if Microphone.decibel < 30:
            Microphone.decibel = 30
        elif Microphone.decibel > 100:
            Microphone.decibel = 100


