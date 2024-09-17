import os
import shutil

audio_input_dire = './all_audios'
trans_dire = './all_trans'

if os.path.exists(trans_dire):
    shutil.rmtree(trans_dire)

os.mkdir(trans_dire)

# for audio_file in os.listdir(audio_input_dire):
os.system('whisper {0} --output_dir {1} --output_format txt --language en --threads 12'.format(
    os.path.join(audio_input_dire, '*.flac'),
    trans_dire
))
