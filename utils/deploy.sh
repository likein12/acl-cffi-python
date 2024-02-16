#! /bin/bash
cd $1
if [ $2 = "build" ]; then
    pypy3 -mpip install -e .
fi
tar czvf acl-cffi-python.tar.gz  -T <(IFS=$'\n'; printf '%s\n' $(<embedding_file_list.txt))
pypy3 ./utils/deployer.py ./workspace/draft.py
pypy3 ./workspace/Main.py < ./workspace/input.txt
