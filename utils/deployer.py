import os
import sys
import base64


with open('acl-cffi-python.tar.gz','rb') as f:
    tar_binary = base64.b85encode(f.read())

code = "".join("\t" + line for line in open(sys.argv[1], "r"))

whole_code = """# created by https://github.com/likein12/acl-cffi-python
import sys

if len(sys.argv) >= 2 and sys.argv[1] == "ONLINE_JUDGE":
    import base64
    tar_binary = TARBINARY

    with open('acl-cffi-python.tar.gz','wb') as f:
        f.write(base64.b85decode(tar_binary))
        
    import os
    
    os.system("tar -zxvf acl-cffi-python.tar.gz")
    os.system("pypy3 -mpip install -e .")
else:
CODE
""".replace("TARBINARY", str(tar_binary)).replace("CODE", code)

open("Main.py", "w").write(whole_code)