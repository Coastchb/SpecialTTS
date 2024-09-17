speaker_id='f001'
raw_vidoe_dir='raw_videos'
raw_audio_dir='extracted_audios'
map_file='filename_maps.txt'

#
python data_preprocess.py

#
python segment_audio.py

#
python process_segment.py

#
python get_tracsript.py

#
# python select_target_files.py