#! /bin/bash
cd ..
pypy3 -mpip install -e .
tar czvf acl-cffi-python.tar.gz  -T <(IFS=$'\n'; printf '%s\n' $(<embedding_file_list.txt))
pypy3 ./utils/deployer.py ./utils/$1