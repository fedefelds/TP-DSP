import librosa
import numpy as np
filename='/Users/Fede/Desktop/stew.mp3'
y, sr = librosa.load(filename)
intervals=librosa.effects.split(y, top_db=60, ref=np.amax, frame_length=1024, hop_length=50)
M_s=0
for i in range(0,intervals.shape[0]):
    M_s = M_s+intervals[i,1]-intervals[i,0]
N=len(y)
SR=((N-M_s)/N)
print(SR)