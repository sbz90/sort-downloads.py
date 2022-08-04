# sort-downloads.py
*Learning Python, not an expert!*

**the forward-slashes in directory variables only work for linux and macOS. For Windows you will have to use backslashes**

## What is it doing?
Checks the Users Downloads Directory and moves downloaded files regarding the file extension.

Can be easily extended for different file extensions

I use [incron](https://packages.debian.org/buster/incron) to run the script on new downloads:
```
simon@pop-os:~$ incrontab -l

<src_dir>	IN_CREATE	<path_to_sort-downloads.py>
```
the script obviously needs to be executable for the incron-user.
