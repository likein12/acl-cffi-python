# created by https://github.com/likein12/acl-cffi-python
import sys

if len(sys.argv) >= 2 and sys.argv[1] == "ONLINE_JUDGE":
    import base64
    tar_binary = b'ABzY80000000Zs80Sy2E0K%a6Pi+o2pa1{>00000004kD1Df6)Cjck_00'

    with open('acl-cffi-python.tar.gz','wb') as f:
        f.write(base64.b85decode(tar_binary))
        
    import os
    
    os.system("tar -zxvf acl-cffi-python.tar.gz")
    os.system("pypy3 -mpip install -e .")
else:
	print("Yo")
