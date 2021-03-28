
import os
from shutil import copyfile


src_root=r"/home/aihomes/Documents/Uday/Data/valid" 
dst_root=r"/home/aihomes/Documents/Uday/Data/valid_2imageset" 

for cur_dir in range(1,129):
  if not os.path.exists(os.path.join(dst_root,str(cur_dir))):
    os.makedirs(os.path.join(dst_root,str(cur_dir)))
  src_path=os.path.join(src_root,str(cur_dir))
  im_names=[f for f in os.listdir(src_path)]
  for f in range(0,2):
    copyfile(os.path.join(src_path,im_names[f]), os.path.join(dst_root,str(cur_dir),im_names[f]))               
