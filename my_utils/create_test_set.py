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

src_root=r"/mnt/sdb1/Uday/Images/test" 
dst_root=r"/mnt/sdb1/Uday/Images/test_128classes" 

im_names=[f for f in os.listdir(src_root)]
img_cnt=0;
for cur_dir in range(1,129):
    if not os.path.exists(os.path.join(dst_root,str(cur_dir))):
      os.makedirs(os.path.join(dst_root,str(cur_dir)))
    for f in range(0,99):
      copyfile(os.path.join(src_root,im_names[img_cnt]), os.path.join(dst_root,str(cur_dir),im_names[img_cnt]))
      img_cnt=img_cnt+1 
initia_val=img_cnt
for f in range(initia_val,len(im_names)):              
  copyfile(os.path.join(src_root,im_names[img_cnt]), os.path.join(dst_root,str(128),im_names[img_cnt]))
  img_cnt=img_cnt+1
