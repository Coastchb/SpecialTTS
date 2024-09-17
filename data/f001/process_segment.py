import os
import shutil

seg_dire = './segments'
audio_input_dire = './extracted_audios'
audio_output_dire = './all_audios'

target_gender = 'female'
min_nonsilence_duration = 3.0
max_nonsilence_duration = 12.0
max_silence_duration = 1.0
# valid_pitch = 2.0

if os.path.exists(audio_output_dire):
    shutil.rmtree(audio_output_dire)
os.mkdir(audio_output_dire)


for filename in os.listdir(seg_dire):
    if not filename.endswith('csv'):
        continue
    filename = filename.split('.')[0]
    input_file = os.path.join(seg_dire, filename + '.csv')
    output_file = os.path.join(seg_dire, filename + '.txt')
    long_pitch_file = os.path.join(seg_dire, 'long_pitch_' + filename + '.txt')

    final_ret = []
    cur_ret = -1
    for line in open(input_file).readlines()[1:]:
        label, start, end = line.strip().split('\t')
        start = float(start)
        end = float(end)
        print('line:{0}'.format(line))

        if label == target_gender:
            if (end - start) >= min_nonsilence_duration:
                if (cur_ret > -1) and ((start - cur_ret) >= min_nonsilence_duration):
                    final_ret.append((cur_ret, start))
                final_ret.append((start, end))
                cur_ret = -1
            else:
                if cur_ret == -1:
                    cur_ret = start

        if label == 'noise':
            if (cur_ret > -1) and ((start - cur_ret) >= min_nonsilence_duration):
                final_ret.append((cur_ret, start))
            cur_ret = -1

        if (label == 'noEnergy') and ((end - start) >= max_silence_duration):
            if (cur_ret > -1) and ((start - cur_ret) >= min_nonsilence_duration):
                final_ret.append((cur_ret, start))
            cur_ret = -1

    if (cur_ret > -1) and ((end - cur_ret) >= min_nonsilence_duration):
        final_ret.append((cur_ret, end))

    with open(output_file, 'w') as fd:
        fd.writelines('\n'.join([','.join([str(y) for y in x]) for x in final_ret]))

    def format_time(input_time):
        minute, second = int(input_time // 60), input_time % 60
        return minute, second

    audio_input_file = os.path.join(audio_input_dire, filename + '.flac')
    audio_output_file_prefix = os.path.join(audio_output_dire, filename)
    long_pitchs = []
    for seg_idx, (start, end) in enumerate(final_ret):
        if end - start >= max_nonsilence_duration:
            long_pitchs.append('{0},{1}'.format(start, end))
            continue
        audio_output_file = audio_output_file_prefix + '_' + str(seg_idx) + '.flac'
        start_minute, start_second = format_time(start)
        os.system('ffmpeg -i {0} -ss 00:{1}:{2} -t 00:00:{3} {4}'.format(audio_input_file, start_minute, start_second, end-start, audio_output_file))

    if os.path.exists(long_pitch_file):
        os.remove(long_pitch_file)

    with open(long_pitch_file, 'w') as fd:
        fd.writelines('\n'.join(long_pitchs))