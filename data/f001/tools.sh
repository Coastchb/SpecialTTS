#ffmpeg -i cn_0.mp4 -vn  cn_0.wav

# get a_left.flac audio a.flac with 22050 sampling rate, 16-bit precision and left channel
ffmpeg -i a.flac -ar 22050 -sample_fmt s16  -ac 1 -af "pan=stereo|c0=FL"  a_left.flac

# transcribe
whisper 0.mp3 --language en

# segment
ffmpeg -i extracted_wavs/f001_001_mic1.flac -ss 00:0:5.98 -t 00:00:0.48  output.flac

# show audio info
ffprobe a.flac
soxi a.flac

# conda activate python3.8

# female speaker: https://x.com/ursmutlibrarian
# male speaker: https://x.com/UrSwitchyBf