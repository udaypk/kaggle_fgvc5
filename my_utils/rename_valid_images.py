
import os
from shutil import copyfile

src_root=r"/home/aihomes/Documents/Uday/Data/valid_old" 
dst_root=r"/home/aihomes/Documents/Uday/Data/valid_new" 

for cur_dir in range(1,129):
  if not os.path.exists(os.path.join(dst_root,'valid',str(cur_dir))):
    os.makedirs(os.path.join(dst_root,'valid',str(cur_dir)))
  if not os.path.exists(os.path.join(dst_root,'valid_flip',str(cur_dir))):
    os.makedirs(os.path.join(dst_root,'valid_flip',str(cur_dir)))
  if not os.path.exists(os.path.join(dst_root,'valid_flip_combined',str(cur_dir))):
    os.makedirs(os.path.join(dst_root,'valid_flip_combined',str(cur_dir)))


  src_path1=os.path.join(src_root,'valid',str(cur_dir))
  im_names1=[f for f in os.listdir(src_path1)]
  src_path2=os.path.join(src_root,'valid_flip',str(cur_dir))
  im_names2=[f for f in os.listdir(src_path2)]
  src_path3=os.path.join(src_root,'valid_flip_combined',str(cur_dir))
  im_names3=[f for f in os.listdir(src_path3)]

  img_cnt=1; 
  for f in im_names1:
    copyfile(os.path.join(src_path1,f), os.path.join(dst_root,'valid',str(cur_dir),str(((cur_dir-1)*100)+img_cnt).zfill(5)+'.jpeg'))
    copyfile(os.path.join(src_path2,f), os.path.join(dst_root,'valid_flip',str(cur_dir),str(((cur_dir-1)*100)+img_cnt).zfill(5)+'.jpeg'))
    copyfile(os.path.join(src_path3,f), os.path.join(dst_root,'valid_flip_combined',str(cur_dir),str(((cur_dir-1)*100)+img_cnt).zfill(5)+'.jpeg'))
    img_cnt=img_cnt+1;               
