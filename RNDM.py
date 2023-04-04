import os,platform
os.system('git pull')
 
yaseen=platform.architecture()[0]
if yaseen=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif yaseen=="64bit":
    __import__("yaseen1")
