import os

input_dir = '普通语调/trans'

valid_cnt = 0
invalid_cnt = 0
for f in os.listdir(input_dir):
    f_path = os.path.join(input_dir, f)
    f_lines = len(open(f_path).readlines())

    if f_lines != 1:
        invalid_cnt += 1
        print(f_path)
    else:
        valid_cnt += 1

print('valid_cnt:', valid_cnt)
print('invalid_cnt:', invalid_cnt)

