Source:
 - https://askubuntu.com/questions/1450426/need-gcc-and-g-4-8-in-ubuntu-22-04-1

Command:
```
sudo apt install ./<filename>.deb
```

--5.5--
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/g++-5_5.5.0-12ubuntu1_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/libstdc++-5-dev_5.5.0-12ubuntu1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/gcc-5-base_5.5.0-12ubuntu1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/gcc-5_5.5.0-12ubuntu1_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/libgcc-5-dev_5.5.0-12ubuntu1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/cpp-5_5.5.0-12ubuntu1_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/libasan2_5.5.0-12ubuntu1_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-5/libmpx0_5.5.0-12ubuntu1_amd64.deb
```


--4.8.5--
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/g++-4.8_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/libstdc++-4.8-dev_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/gcc-4.8-base_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/gcc-4.8_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/libgcc-4.8-dev_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/cpp-4.8_4.8.5-4ubuntu8_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.8/libasan0_4.8.5-4ubuntu8_amd64.deb  
```

--4.9.3--
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/g++-4.9_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/libstdc++-4.9-dev_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/gcc-4.9-base_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/gcc-4.9_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/libgcc-4.9-dev_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/cpp-4.9_4.9.3-13ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.9/libasan1_4.9.3-13ubuntu2_amd64.deb 
sudo apt install ./g++-4.9_4.9.3-13ubuntu2_amd64.deb ./libstdc++-4.9-dev_4.9.3-13ubuntu2_amd64.deb ./gcc-4.9-base_4.9.3-13ubuntu2_amd64.deb ./gcc-4.9_4.9.3-13ubuntu2_amd64.deb ./libgcc-4.9-dev_4.9.3-13ubuntu2_amd64.deb ./cpp-4.9_4.9.3-13ubuntu2_amd64.deb ./libasan1_4.9.3-13ubuntu2_amd64.deb 
```

--4.7.4-- (COMPLETED by installing the missing packages in this website https://launchpad.net/ubuntu/xenial/amd64/libcloog-pplv4-1/0.16.1-6ubuntu3)
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/g++-4.7_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/libstdc++6-4.7-dev_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/gcc-4.7-base_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/gcc-4.7_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/libgcc-4.7-dev_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/cpp-4.7_4.7.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.7/libobjc-4.7-dev_4.7.4-3ubuntu12_amd64.deb
sudo apt install ./g++-4.7_4.7.4-3ubuntu12_amd64.deb ./libstdc++6-4.7-dev_4.7.4-3ubuntu12_amd64.deb ./gcc-4.7-base_4.7.4-3ubuntu12_amd64.deb ./gcc-4.7_4.7.4-3ubuntu12_amd64.deb ./libgcc-4.7-dev_4.7.4-3ubuntu12_amd64.deb ./cpp-4.7_4.7.4-3ubuntu12_amd64.deb ./libobjc-4.7-dev_4.7.4-3ubuntu12_amd64.deb
```

--4.6.4--
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/g++-4.6_4.6.4-6ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/libstdc++6-4.6-dev_4.6.4-6ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/gcc-4.6-base_4.6.4-6ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/gcc-4.6_4.6.4-6ubuntu2_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/libgcc-4.6-dev_4.6.4-3ubuntu12_amd64.deb
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-4.6/cpp-4.6_4.6.4-6ubuntu2_amd64.deb
sudo apt install ./g++-4.6_4.6.4-6ubuntu2_amd64.deb ./libstdc++6-4.6-dev_4.6.4-6ubuntu2_amd64.deb ./gcc-4.6-base_4.6.4-6ubuntu2_amd64.deb ./gcc-4.6_4.6.4-6ubuntu2_amd64.deb ./libgcc-4.6-dev_4.6.4-3ubuntu12_amd64.deb ./cpp-4.6_4.6.4-6ubuntu2_amd64.deb
```

--3.3.6--(MISSING)
```
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/gcc-3.3_3.3.6ds1-25ubuntu4.dsc
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/libstdc++5_3.3.6-28ubuntu1_amd64.deb 
wget http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/gcc-3.3_3.3.6ds1.orig.tar.gz
```


