# Load the API
import os

from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

input_dire = './extracted_audios'
output_dire = './segments'
for input_filename in os.listdir(input_dire):
    input_file = os.path.join(input_dire, input_filename)
    seg = Segmenter()
    segmentation = seg(input_file)
    print(segmentation)

    seg2csv(segmentation, '{0}.csv'.format(os.path.join(output_dire, input_filename.split('.')[0])))
