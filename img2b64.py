#!/usr/bin/python


import os
import sys
from encodings import base64_codec
print '''
#Author:S4AD
#usage:
  Windows:
    $:python img2b64.py
     IMG2B64(img_path)>c:\\users\\user\\desktop\\img.jpeg or .jpg .png .gif ...etc
     
  Linux:
    $:chmod 777 img2b64.py;python img2b64.py
     IMG2B64(img_path)>/home/user/Desktop/img.jpeg or .jpg .png .gif ...etc

'''

line_2="IMG2B64(img_path)>"
line2=raw_input(line_2)


v = open(line2).read()
ev="IMG2B64(generated_html_code)>\ndata:image/jpg;base64,\n%s"%(base64_codec.base64.encodestring(v))
print ev
exit()







