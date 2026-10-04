from pathlib import Path
import sys, subprocess, wave
import numpy as np
sys.path.insert(0,str(Path('output/video-tools').resolve()))
import imageio_ffmpeg
out=Path('output/knowledge-university')
with wave.open(str(out/'intro-logo-music.wav'),'rb') as w:
    sr=w.getframerate(); samples=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').reshape(-1,2).astype(np.float64)
# Move the first bell onset from 0.35 s to 0.40 s, and remove the earlier pad lead-in.
delay=round(.05*sr)
a=np.zeros_like(samples); a[delay:]=samples[:-delay]
start=round(.4*sr); a[:start]=0
attack=round(.012*sr); a[start:start+attack]*=np.linspace(0,1,attack)[:,None]
release=round(.05*sr); a[-release:]*=np.linspace(1,0,release)[:,None]
audio=out/'intro-logo-music-synced.wav'
with wave.open(str(audio),'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.rint(a).astype('<i2').tobytes())
video=out/'knowledge-university-intro-synced-720p.mp4'
ff=imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([ff,'-y','-loglevel','error','-i',str(out/'knowledge-university-logo-intro-cream-fast-720p.mp4'),'-i',str(audio),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-t','6','-movflags','+faststart',str(video)],check=True)
r=subprocess.run([ff,'-i',str(video),'-f','null','-'],capture_output=True,text=True)
assert r.returncode==0
print(r.stderr[-2200:])
print('First nonzero source audio sample (seconds):',np.flatnonzero(np.any(a!=0,axis=1))[0]/sr)
print(video.resolve())
