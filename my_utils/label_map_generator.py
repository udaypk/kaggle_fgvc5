import os
from shutil import copyfile
label_map_file = open("furnit_label_map.pbtxt", "w")
for i in range(1,129):
  temp_str="item {\n"
  label_map_file.write(temp_str)
  temp_str="  id: "+str(i)+"\n"
  label_map_file.write(temp_str)
  temp_str="  name: "+"\'"+str(i)+"\'"+"\n"
  label_map_file.write(temp_str)
  temp_str="}\n\n"
  label_map_file.write(temp_str)

label_map_file.close()

