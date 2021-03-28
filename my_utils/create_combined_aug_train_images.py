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
import random


train_valid_root=r"/mnt/sdb1/Uday/Images/latest_train/train_and_valid" 
aug_root=r"/mnt/sdb1/Uday/Images/latest_train"


img_cnt=0;
for cur_dir in range(1,128):
    print("Copying directory:"+str(cur_dir)) 
    train_valid_im_names=[f for f in os.listdir(os.path.join(train_valid_root,str(cur_dir))) if os.path.isfile(os.path.join(train_valid_root,str(cur_dir),f))]
    num_images=len(train_valid_im_names)
    aug1_img_cnt=0
    aug2_img_cnt=0
    aug3_img_cnt=0
    if (num_images<=1200):
        for f in train_valid_im_names:
            copyfile(os.path.join(train_valid_root,str(cur_dir),f), os.path.join(aug_root,'train_valid_aug_1',str(cur_dir),f))
            copyfile(os.path.join(train_valid_root,str(cur_dir),f), os.path.join(aug_root,'train_valid_aug_2',str(cur_dir),f))
            copyfile(os.path.join(train_valid_root,str(cur_dir),f), os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),f))
    else:
        random.shuffle(train_valid_im_names)
        for i in range(0,1200):
            copyfile(os.path.join(train_valid_root,str(cur_dir),train_valid_im_names[i]), os.path.join(aug_root,'train_valid_aug_1',str(cur_dir),train_valid_im_names[i]))
        random.shuffle(train_valid_im_names)
        for i in range(0,1200):
            copyfile(os.path.join(train_valid_root,str(cur_dir),train_valid_im_names[i]), os.path.join(aug_root,'train_valid_aug_2',str(cur_dir),train_valid_im_names[i]))
        random.shuffle(train_valid_im_names)
        for i in range(0,1200):
            copyfile(os.path.join(train_valid_root,str(cur_dir),train_valid_im_names[i]), os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),train_valid_im_names[i]))
















        
