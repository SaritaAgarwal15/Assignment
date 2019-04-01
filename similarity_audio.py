
import acoustid
import chromaprint
import numpy as np


import os
import glob
path1 = input('Enter path 1:')
path2 = input('Enter path 2:')



P1= glob.glob(os.path.join(path1, '*.mp3'))
P2= glob.glob(os.path.join(path2, '*.mp3'))



duration, fp_encoded = acoustid.fingerprint_file(P1[0])
fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)

duration, fp_encoded = acoustid.fingerprint_file(P2[0])
sample_fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)
#print(fingerprint)


from fuzzywuzzy import fuzz
similarity = fuzz.ratio(sample_fingerprint, fingerprint)
print(str(similarity)+str("%"))
print("end")
