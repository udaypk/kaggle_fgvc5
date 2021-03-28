import os
import subprocess
import shlex

src_path=r"/mnt/sdb1/Uday/training_models_bkup/furnit_aug1/trainall_inception_resnetv2_aug_3600_aug_1_1/bkup"
#src_path=r"/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/furnit_aug1/trainall_inception_resnetv2_aug_1data_90epochs"



line1= "model_checkpoint_path: \""+src_path+"/"
line2="all_model_checkpoint_paths: \""+src_path+"/"

src_file_names=[f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path,f)) and 'meta' in f]
src_file_names.sort(key=lambda f: int(filter(str.isdigit, f)))
count=1
for f in src_file_names:  
  if count>=1 :
    ckpt_file = open(os.path.join(src_path,"checkpoint"), "w")     
    ckpt_name=os.path.splitext(f)[0]
    print(ckpt_name)
    ckpt_file.write(line1+ckpt_name+"\"\n")
    ckpt_file.write(line2+ckpt_name+"\"\n")
    ckpt_file.close()
    count=0
    os.system('sh aug1_inception_resnet_v2.sh')
    #subprocess.call(shlex.split('./aug1_inception_resnet_v2.sh')) 
  count=count+1

