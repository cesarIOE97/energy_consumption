# C++

Compilers | Version | Release date    | First release | Status
------------|---------|-----------------|---------------|-------
 GCC and G++ | 13.1 | 2023-04-26 | 2023-04-26 | release............(x)...(x)
 GCC and G++ | 12.3 | 2023-05-08 | 2022-05-06 | release............(x)...(x)
 GCC and G++ | 11.4 | 2023-05-29 | 2021-04-27 | release............(x)...(x) 11.3
 GCC and G++ | 10.4 | 2022-06.28 | 2020-05-07 | release............(x)...(x)
 GCC and G++ | 9.5 | 2022-05-27 | 2019-05-03 | release.............(x)...(x)
 GCC and G++ | 8.5 | 2021-05-14 | 2018-05-02 | release.............(x)...(x)   ..... tar gz
 GCC and G++ | 7.5 | 2019-11-14 | 2017-05-02 | release.............(x)...(x)   ..... tar gz
 GCC and G++ | 6.5 | 2018-10-26 | 2016-04-27 | release.............(x)...(x)   ..... tar gz
 GCC and G++ | 5.5 | 2017-10-10 | 2015-04-22 | release.............(x)...(x)
 GCC and G++ | 4.9.4 | 2016-08-03 | 2014-04-22 | release...........(x)...(x)
 GCC and G++ | 4.8.5 | 2015-06-23 | 2013-03-22 | release...........(x)...(x)
 GCC and G++ | 4.7.4 | 2014-06-12 | 2012-03-22 | release...........(x)...(x)
 GCC and G++ | 4.6.4 | 2013-04-12 | 2011-03-25 | release...........(x)...(x)
 GCC and G++ | 4.5.4 | 2012-07-02 | 2010-04-14 | release
 GCC and G++ | 4.4.7 | 2012-03-13 | 2009-10-15 | release...........(x)...(x)
 GCC and G++ | 4.3.6 | 2011-06-27 | 2008-03-05 | release
 GCC and G++ | 4.2.4 | 2008-05-19 | 2007-05-13 | release
 GCC and G++ | 4.1.2 | 2007-02-13 | 2006-02-28 | release
 GCC and G++ | 4.0.4 | 2007-01-31 | 2005-04-20 | release
 GCC and G++ | 3.4.6 | 2006-03-06 | 2004-04-18 | release
 GCC and G++ | 3.3.6 | 2005-05-03 | 2003-05-13 | release
 GCC and G++ | 3.2.3 | 2003-04-22 | 2002-08-14 | release
 GCC and G++ | 3.0.4 | 2002-02-20 | 2001-01-18 | release .......... Configuration x86_64-unknown-linux-gnu not supported



Source:
 - [GCC Releases](https://gcc.gnu.org/releases.html)
 - [GCC Development Plan](https://gcc.gnu.org/develop.html)
 - [C++ Compiler Support](https://en.cppreference.com/w/cpp/compiler_support#References)

## Mul




Options for multi versions of C++

sudo update-alternatives --remove-all gcc 
sudo update-alternatives --remove-all g++


sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 7
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 7
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9

https://www.fosslinux.com/39386/how-to-install-multiple-versions-of-gcc-and-g-on-ubuntu-20-04.htm
https://askubuntu.com/questions/26498/how-to-choose-the-default-gcc-and-g-version





UNINSTALL GCC

sudo apt-get install --reinstall gcc-
sudo apt-get purge gcc-
sudo apt-get --purge remove gcc-



TO INSTALL GCC-5
echo "deb http://old-releases.ubuntu.com/ubuntu zesty main" | sudo tee /etc/apt/sources.list.d/zesty.list
sudo apt-add-repository -r universe
sudo apt update
sudo apt install gcc-5
