#!/usr/bin/env python3

# import modules
import getpass
import os
import shutil

# get username
username = getpass.getuser()
# define variables for directorys
src_path = "/home/{}/Downloads".format(username)
dst_path_images = "/home/{}/Bilder/Downloads".format(username)
dst_path_isos = "/home/{}/Isos/Downloads".format(username)
dst_path_documents = "/home/{}/Dokumente/Downloads".format(username)
dst_path_archives = "/home/{}/Downloads/Archives".format(username)


# check whether specified destinations exist and create it if necessary
dst_path_images_exists = os.path.exists(dst_path_images)
dst_path_isos_exists = os.path.exists(dst_path_isos)
dst_path_documents_exists = os.path.exists(dst_path_documents)
dst_path_archives_exists = os.path.exists(dst_path_archives)


if not dst_path_images_exists:
    os.makedirs(dst_path_images)
    
if not dst_path_isos_exists:
    os.makedirs(dst_path_isos)
    
if not dst_path_documents_exists:
    os.makedirs(dst_path_documents)

if not dst_path_archives_exists:
    os.makedirs(dst_path_archives)
    

# save list of files as sourcefiles
sourcefiles = os.listdir(src_path)

# check each file extension and move the file to correct dst_path
for file in sourcefiles:
    if file.endswith('.iso'):
        shutil.move(os.path.join(src_path,file), os.path.join(dst_path_isos,file))
    elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
        shutil.move(os.path.join(src_path,file), os.path.join(dst_path_images,file))
    elif file.endswith('.txt') or file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.xlsx') or file.endswith('.csv'):
        shutil.move(os.path.join(src_path,file), os.path.join(dst_path_documents,file))
    elif file.endswith('.zip') or file.endswith('.rar') or file.endswith('.gz') or file.endswith('.tgz'):
        shutil.move(os.path.join(src_path,file), os.path.join(dst_path_archives,file))