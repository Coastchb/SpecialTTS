import os

input_file = './myseg.csv'
target_gender = 'female'
valid_interval = 5.0
valid_silence = 1.0
valid_pitch = 2.0

final_ret = []
cur_ret = -1
for line in open(input_file).readlines()[1:]:
    label, start, end = line.strip().split('\t')
    start = float(start)
    end = float(end)
    print('line:{0}'.format(line))

    if label == target_gender:
        if (end - start) >= valid_interval:
            if (cur_ret > -1) and ((start - cur_ret) >= valid_interval):
                final_ret.append((cur_ret, start))
            final_ret.append((start, end))
            cur_ret = -1
        else:
            if cur_ret == -1:
                cur_ret = start

    if label == 'noise':
        if (cur_ret > -1) and ((start - cur_ret) >= valid_interval):
            final_ret.append((cur_ret, start))
        cur_ret = -1

    if (label == 'noEnergy') and ((end - start) >= valid_silence):
        if (cur_ret > -1) and ((start - cur_ret) >= valid_interval):
            final_ret.append((cur_ret, start))
        cur_ret = -1

if (cur_ret > -1) and ((end - cur_ret) >= valid_interval):
    final_ret.append((cur_ret, end))

print(final_ret)
