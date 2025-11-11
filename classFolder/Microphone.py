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

    tresholdTalk = 50 # ref decibel used for unable mouth when talk.
    tresholdTalkMid = 30 # ref decibel used for mouth mid open.


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

            currentDecibel += 55
            currentDecibel *= 1.8518
            currentDecibel = max(0.0001, min(currentDecibel, 99.9999))

        # acumulation.
        Microphone.decibel *= 0.35
        Microphone.decibel += (currentDecibel * 0.75)
        Microphone.decibel = max(0.0001, min(Microphone.decibel, 99.9999))
        print(f"${currentDecibel} --- ${Microphone.decibel}")



