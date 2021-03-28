import os
import random
src_root=r"/media/ailab/TRANSCENDSJ/ImageClassification/latest_train/train_valid_aug_max" 
train_count=0
for cur_dir in range(1,129):
  im_names = [f for f in os.listdir(os.path.join(src_root,str(cur_dir))) if os.path.isfile(os.path.join(src_root,str(cur_dir),f))]
  #train_count=train_count+len(im_names) 
  print(len(im_names))    
  #if (len(im_names)<1600):          
  #  print(len(im_names))
  #im_names_new=im_names+random.shuffle(im_names)
  #print(im_names[0])
  #print(len([im_names,random.shuffle(im_names)]))
#print(train_count)
