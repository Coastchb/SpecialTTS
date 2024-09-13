# Load the API
from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

media = './extracted_wavs/f001_001_mic1.flac'
seg = Segmenter()
segmentation = seg(media)
print(segmentation)

seg2csv(segmentation, 'myseg.csv')
