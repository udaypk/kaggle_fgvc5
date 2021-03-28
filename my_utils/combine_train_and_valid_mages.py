'''
#Copy images from train_chunk0, chunk1 etc to train_128classes folder
import os
from shutil import copyfile

src_root=r"/mnt/sdb1/Uday/Images/train_chunk" 
dst_root=r"/mnt/sdb1/Uday/Images/train_128classes" 

for cur_dir in range(1,129):
  if not os.path.exists(os.path.join(dst_root,str(cur_dir))):
    os.makedirs(os.path.join(dst_root,str(cur_dir)))

  for train_dir in range(0,7):
    src_path=os.path.join(src_root+str(train_dir),str(cur_dir))
    im_names=[f for f in os.listdir(src_path)]
    for f in im_names:
      copyfile(os.path.join(src_path,f), os.path.join(dst_root,str(cur_dir),"Class_"+str(cur_dir).zfill(3)+"_"+f))
'''


import os
from shutil import copyfile

train_root=r"/mnt/sdb1/Uday/Images/train_128classes" 
train_valid_root=r"/mnt/sdb1/Uday/Images/latest_train/train_and_valid" 

for cur_dir in range(1,129):
  train_im_names=[f for f in os.listdir(os.path.join(train_root,str(cur_dir))) if os.path.isfile(os.path.join(train_root,str(cur_dir),f))]
  for f in train_im_names:
    copyfile(os.path.join(train_root,str(cur_dir),f), os.path.join(train_valid_root,str(cur_dir),f))               
