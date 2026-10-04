from pathlib import Path
import sys, subprocess, wave
import numpy as np
from PIL import Image
sys.path.insert(0,str(Path('output/video-tools').resolve()))
import imageio_ffmpeg
out=Path('output/knowledge-university')
ff=imageio_ffmpeg.get_ffmpeg_exe()
def smooth(x):
    x=np.clip(x,0,1); return x*x*(3-2*x)
# Original short bell-and-warm-pad musical cue, synthesized locally.
sr=48000; tt=np.arange(6*sr)/sr
music=np.zeros((len(tt),2),dtype=np.float64)
for start,midi,amp in [(0.35,60,.10),(.85,64,.11),(1.35,67,.12),(1.9,72,.15),(2.5,76,.10),(3.15,74,.08),(3.65,72,.12)]:
    u=np.maximum(tt-start,0); f=440*2**((midi-69)/12)
    env=(1-np.exp(-u*100))*np.exp(-u/1.05)*(tt>=start)
    tone=(np.sin(2*np.pi*f*u)+.26*np.sin(2*np.pi*2*f*u)*np.exp(-u*2)+.09*np.sin(2*np.pi*3*f*u))*env*amp
    music[:,0]+=tone; music[:,1]+=tone*.94
    delay=int(.145*sr); music[delay:,1]+=tone[:-delay]*.16
for f in [130.8128,164.8138,195.9977]:
    pad=.022*np.sin(2*np.pi*f*tt)*smooth(tt/1.4)*(1-smooth((tt-4.4)/1.5))
    music+=pad[:,None]
music*= (smooth(tt/.15)*(1-smooth((tt-4.8)/1.18)))[:,None]
music*=.72/max(np.max(np.abs(music)),.72)
audio=out/'intro-logo-music.wav'
with wave.open(str(audio),'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((music*32767).astype('<i2').tobytes())
source=Image.open(r'C:/Users/user/Desktop/지식대학/지식대학 프로필 이미지.png').convert('RGBA').resize((600,600),Image.Resampling.LANCZOS)
src=np.asarray(source,dtype=np.float32)
# Isolate the original blue lettering/emblem and gold dot without redrawing them.
r,g,b=src[:,:,0],src[:,:,1],src[:,:,2]
blue=np.clip((b-r-15)/45,0,1)
gold=np.clip((r-b-45)/65,0,1)*np.clip((g-b-25)/60,0,1)
ink=np.maximum(blue,gold)*(src[:,:,3]/255)
y,x=np.mgrid[:720,:1280]; dist=np.sqrt((x-639.5)**2+(y-359.5)**2)
disk=np.clip(287.5-dist,0,1)[:,:,None]
base=np.empty((720,1280,3),np.float32); base[:]=[222,239,252]
base[:]=[255,251,232]
video=out/'knowledge-university-logo-intro-cream-720p.mp4'
p=subprocess.Popen([ff,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','1280x720','-r','30','-i','-','-i',str(audio),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-t','6','-movflags','+faststart',str(video)],stdin=subprocess.PIPE,stderr=subprocess.PIPE)
thumbs=[]
for i in range(180):
    t=i/30; frame=base.copy()
    reveal=smooth((t-.85)/1.25)
    region=frame[60:660,340:940]
    a=(ink*reveal)[:,:,None]
    region[:]=region*(1-a)+src[:,:,:3]*a
    gain=smooth(t/.45)*(1-smooth((t-5.05)/(179/30-5.05)))
    arr=np.rint(frame*gain).astype(np.uint8)
    p.stdin.write(arr.tobytes())
    if i in [18,36,54,90,156,179]: thumbs.append(Image.fromarray(arr).resize((384,216)))
p.stdin.close(); err=p.stderr.read(); rc=p.wait()
if rc: raise RuntimeError(err.decode(errors='replace'))
sheet=Image.new('RGB',(1152,432))
for n,im in enumerate(thumbs): sheet.paste(im,((n%3)*384,(n//3)*216))
sheet.save(out/'intro-logo-cream-contact-sheet.jpg')
check=subprocess.run([ff,'-i',str(video),'-f','null','-'],capture_output=True,text=True)
print(check.stderr[-2400:]); print(video.resolve())

