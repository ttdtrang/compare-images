import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test', help='test image')
parser.add_argument('--truth', help='ground truth image')
args = parser.parse_args()

import numpy as np
import nibabel
from skimage import morphology 
import json

imgTest = nibabel.load(args.test).get_data()
imgTruth = nibabel.load(args.truth).get_data()
jaccard = np.sum(imgTruth == imgTest)*1.0 / np.prod(imgTest.shape)
sorensen = np.sum(imgTruth == imgTest)*2.0 / (np.prod(imgTest.shape) + np.prod(imgTruth.shape))

output = { 
"Jaccard": ("%s" % jaccard),
"Sorensen": ("%s" % sorensen) 
}
print(json.dumps(output))
