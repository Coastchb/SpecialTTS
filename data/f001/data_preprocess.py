import os
import shutil

speaker_id = 'f001'
raw_vidoe_dir = 'raw_videos'
raw_wav_dir = 'extracted_wavs'
map_file = 'filename_maps.txt'

sampling_rate = 22050
sample_fmt = 's16'

if not os.path.exists(raw_vidoe_dir):
    print('Error: raw video dir {0} not exist!'.format(raw_vidoe_dir))
    exit(-1)

if os.path.exists(raw_wav_dir):
    shutil.rmtree(raw_wav_dir)
os.makedirs(raw_wav_dir)

file_cnt = 1
map_info_list = []
for fn in os.listdir(raw_vidoe_dir):
    source_file = os.path.join(raw_vidoe_dir, fn)
    target_filename = '{spk_id}_{f_cnt:03}'.format(spk_id=speaker_id, f_cnt=file_cnt)

    print('processing file:{0}'.format(source_file))
    # print('ffprobe -v error -show_entries stream=channels -select_streams a:0 "{0}"'.format(source_file))
    channel_info = os.popen('ffprobe -v error -show_entries stream=channels -select_streams a:0 "{0}"'.format(source_file))
    is_mono = channel_info.readlines()[1].strip().split('=')[1] == '1'
    if is_mono:
        target_filename = '{0}_mic0.flac'.format(target_filename)
        os.system('ffmpeg -i "{input_file}" -ar {sr} -sample_fmt {sf} {output_file}'.format(
            input_file=source_file,
            sr=sampling_rate,
            sf=sample_fmt,
            output_file=os.path.join(raw_wav_dir, target_filename),
        ))
    else:
        target_filename = '{0}_mic1.flac'.format(target_filename)
        os.system('ffmpeg -i "{input_file}" -ar {sr} -sample_fmt {sf} -ac 1 -af "pan=mono|c0=FL" {output_file}'.format(
            input_file=source_file,
            sr=sampling_rate,
            sf=sample_fmt,
            output_file=os.path.join(raw_wav_dir, target_filename),
        ))
        target_filename = '{0}_mic2.flac'.format(target_filename)
        os.system('ffmpeg -i "{input_file}" -ar {sr} -sample_fmt {sf} -ac 1 -af "pan=mono|c0=FR" {output_file}'.format(
            input_file=source_file,
            sr=sampling_rate,
            sf=sample_fmt,
            output_file=os.path.join(raw_wav_dir, target_filename)
        ))
    file_cnt += 1

    map_info = '{0}: {1}'.format(target_filename, fn)
    map_info_list.append(map_info)

with open('filename_map', 'w') as fd:
    fd.writelines('\n'.join(map_info_list))



