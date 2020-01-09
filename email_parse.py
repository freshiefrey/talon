from talon.signature.learning.dataset import build_extraction_dataset
from talon.signature.learning import classifier as c

build_extraction_dataset("/Users/jeffrey/Desktop/forge/dataset/P", "/Users/jeffrey/Desktop/talon/talon/signature/data/train_forge.data")
c.train(c.init(), "/Users/jeffrey/Desktop/talon/talon/signature/data/train_forge.data", "/Users/jeffrey/Desktop/talon/talon/signature/data/classifier")
