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
for cur_dir in range(1,129):
    print("Copying directory:"+str(cur_dir)) 
    train_valid_im_names=[f for f in os.listdir(os.path.join(train_valid_root,str(cur_dir))) if os.path.isfile(os.path.join(train_valid_root,str(cur_dir),f))]    
    num_images=len(train_valid_im_names)
    if ((num_images>1200) and (num_images<=2400)):
        random.shuffle(train_valid_im_names)        
        for i in range(0,min(num_images,2400)):
            if not os.path.isfile(os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),train_valid_im_names[i])):
                copyfile(os.path.join(train_valid_root,str(cur_dir),train_valid_im_names[i]), os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),train_valid_im_names[i]))
    elif ((num_images>1200) and (num_images>2400)):
        aug_im_names=[f for f in os.listdir(os.path.join(aug_root,'train_valid_aug_3',str(cur_dir))) if os.path.isfile(os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),f))] 
        im_diff=[ f for f in train_valid_im_names if f not in aug_im_names]
        for i in range(0,min(len(im_diff),2400)):
            copyfile(os.path.join(train_valid_root,str(cur_dir),im_diff[i]), os.path.join(aug_root,'train_valid_aug_3',str(cur_dir),im_diff[i]))
















        
