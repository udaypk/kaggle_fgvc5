import os
import time
from shutil import copyfile
train_relative_path=r"furnit_aug1/trainall_inception_resnetv2_aug_3600_aug_1_1"

src_path=os.path.join(r"/home/ailab/Documents/Uday/tensorflow/models/research/slim/data", train_relative_path)
dst_path=os.path.join(r"/mnt/sdb1/Uday/training_models_bkup",train_relative_path,"bkup")

if not os.path.exists(dst_path):
  os.makedirs(dst_path)
print("Sleeping...")
time.sleep(600)
while(True): 
  print("Copying...")
  src_file_names=[f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path,f))]
  dst_file_names=[f for f in os.listdir(dst_path) if os.path.isfile(os.path.join(dst_path,f))]
  for f in src_file_names:
    if not os.path.exists(os.path.join(dst_path,f)) and 'model' in f:
      print(f)
      try:       
        copyfile(os.path.join(src_path,f), os.path.join(dst_path,f))  
      except IOError, e:
        print "Unable to copy file. %s" % e             
  print("Sleeping...")
  time.sleep(3600) 
