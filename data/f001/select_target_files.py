import os
import shutil

audio_input_dire = 'all_audios'
trans_input_dire = 'all_trans'
audio_output_dire = 'audios'
trans_output_dire = 'trans'

#target_file_ids = [3, 4, 8, 12, 14, 15, 17, 21, 22, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 47, 50, 52, 53]
target_file_ids = [55, 56, 58, 59, 60, 61, 69, 71, 72, 74, 77, 79, 81, 82, 88, 89]

print(len(target_file_ids))
for d in [audio_output_dire, trans_output_dire]:
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)

for f in os.listdir(audio_input_dire):
    file_idx = int(f.split('_')[1])
    trans_file = f.replace('flac', 'txt')
    if (file_idx in target_file_ids) and (os.path.exists(os.path.join(trans_input_dire, trans_file))):
        shutil.copyfile(os.path.join(audio_input_dire, f), os.path.join(audio_output_dire, f))
        shutil.copyfile(os.path.join(trans_input_dire, trans_file), os.path.join(trans_output_dire, trans_file))
