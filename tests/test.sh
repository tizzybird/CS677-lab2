#!/bin/bash
username=yensungchen
testServer=elnux3.cs.umass.edu

echo "Start testing test case 1"
bash ./setup.sh
ssh ${username}@${testServer} << 'END_SSH'
set -x
targetPath=./cs677/lab2
cd ${targetPath}/tests
python test1.py
END_SSH
echo "Test case 1 is finished, the result is under tests/test1.txt"
bash ./clear.sh

echo "Start testing test case 2"
bash ./setup2.sh
ssh ${username}@${testServer} << 'END_SSH'
set -x
targetPath=./cs677/lab2
cd ${targetPath}/tests
python test2.py
END_SSH
echo "Test case 2 is finished, the result is under tests/test2.txt"
bash ./clear.sh

echo "Start testing test case 3"
bash ./setup2.sh
ssh ${username}@${testServer} << 'END_SSH'
set -x
targetPath=./cs677/lab2
cd ${targetPath}/tests
python test3.py 1 & python test3.py 2 &
sleep 3
END_SSH
echo "Test case 3 is finished, the result is under tests/test3.txt"
bash ./clear.sh

echo "Start testing test case 4"
bash ./setup3.sh
ssh ${username}@${testServer} << 'END_SSH'
set -x
targetPath=./cs677/lab2
cd ${targetPath}/tests
python test4.py 1 & python test4.py 2 &
sleep 3
END_SSH
echo "Test case 4 is finished, the result is under tests/test4.txt"
bash ./clear.sh
