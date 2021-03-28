from PIL import Image
import os
from shutil import copyfile

src_root=r"/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/furnit/valid" 

for cur_dir in range(1,129):
  src_path=os.path.join(src_root,str(cur_dir))
  im_names=[f for f in os.listdir(src_path)]
  #no_of_images_file.write(str(cur_dir).zfill(3)+"::"+str(len(im_names))+"\n")
  for f in im_names:
    im = Image.open(os.path.join(src_path,f))
    width, height = im.size
    dir_name=cur_dir
    if (width<100) or (height<100) :
      os.remove(os.path.join(src_path,f))
      print("File deleted: "+f)
