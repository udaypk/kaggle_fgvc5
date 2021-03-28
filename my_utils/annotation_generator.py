#x indicates width and y is height
'''
0-filename
1-image width
2-image height
3-object tag
4-xmin
5-ymin
6-xmax
7-ymax

'''


from PIL import Image
import os
from shutil import copyfile

src_root=r"/mnt/sdb1/Uday/Images/train_128classes" 
dst_root=r"/mnt/sdb1/Uday/Images/train/annotations1percent" 
#no_of_images_file = open(r"/mnt/sdb1/Uday/Images/NumberofTrainImages.txt", "w")
for cur_dir in range(1,129):
  src_path=os.path.join(src_root,str(cur_dir))
  im_names=[f for f in os.listdir(src_path)]
  #no_of_images_file.write(str(cur_dir).zfill(3)+"::"+str(len(im_names))+"\n")
  for f in im_names:
    im = Image.open(os.path.join(src_path,f))
    width, height = im.size
    dir_name=cur_dir
    xmin=(width/100)*1
    ymin=(height/100)*1
    xmax=width-xmin
    ymax=height-ymin
    xml_str="<annotation><folder>VOC2012</folder><filename>{0}</filename><source><database>Custom</database><annotation>PASCAL VOC2007</annotation><image>custom</image></source><size><width>{1}</width><height>{2}</height><depth>3</depth></size><segmented>0</segmented><object><name>{3}</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult><bndbox><xmin>{4}</xmin><ymin>{5}</ymin><xmax>{6}</xmax><ymax>{7}</ymax></bndbox></object></annotation>".format(f,width,height,dir_name,xmin,ymin,xmax,ymax)
    if (width>100) and (height>100) :
      annotation_file = open(os.path.join(dst_root,os.path.splitext(f)[0]+".xml"), "w")
      annotation_file.write(xml_str)
      annotation_file.close()  
    else:
      print(os.path.join(src_path,f))

#no_of_images_file.close()













