# sort-downloads.py
*Learning Python, not an expert!*

## What is it doing?
Checks the Users Downloads Directory and moves downloaded files regarding the file extension
Can be easily extended for different file extensions

I use `incron` to run the script on new downloads:
```
simon@pop-os:~$ incrontab -l

<src_dir>	IN_CREATE	<path_to_sort-downloads.py>
```
the script obviously needs to be executable for the incron-user.
