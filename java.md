Interpreters | Version | Release date    | First release | Status
-------------|---------|-----------------|---------------|-------
 CPython | 3.13.0a0  | 2023-06-07 | 2023-06-07 | alpha (preview)
 CPython | 3.12.0b1  | 2023-05-22 | 2023-05-22 | beta (preview)
 CPython | 3.11.3  | 2023-04-05 | 2022-10-24 | bugfix (suppported)
 CPython | 3.10.11 | 2023-04-05 | 2021-10-04 | security (suppported)
 CPython | 3.9.16 | 2022-12-06 | 2020-10-05 | security (suppported)
 CPython | 3.8.16 | 2022-12-06 | 2019-10-14 | security (suppported)
 CPython | 3.7.16 | 2022-12-06 | 2018-06-27 | security (suppported)
 CPython | 3.6.15 | 2021-09-04 | 2016-12-23 | end-of-life (unsupported)
 CPython | 3.5.10 | 2020-09-05 | 2015-09-13 | end-of-life (unsupported)
 CPython | 3.4.10 | 2019-03-18 | 2014-03-16 | end-of-life (unsupported)
 (X) CPython | 3.3.7 | 2017-09-19 | 2012-09-29 | end-of-life (unsupported)
 (X) CPython | 3.2.6 | 2014-10-11 | 2011-02-20 | end-of-life (unsupported)
 (X) CPython | 3.1.5 | 2012-04-09 | 2009-06-27 | end-of-life (unsupported)
 CPython | 3.0.1 | 2009-02-13 | 2008-12-03 | end-of-life (unsupported)
 CPython | 2.7.18 | 2020-04-20 | 2010-07-04 | end-of-life (unsupported)
 (X) CPython | 2.6.9 | 2013-10-29 | 2008-10-01 | end-of-life (unsupported)
 CPython | 2.5.6 | 2011-05-26 | 2006-09-19 | end-of-life (unsupported)


Installation of old and no supported versions

- Download the files from https://jdk.java.net/archive/
  
- Follow the next commands to extract all files:

sudo tar xvf ~/Downloads/openjdk-20.0.2_linux-x64_bin.tar.gz -C /usr/lib/jvm/

- Check the path for both java and javac by verifing their versions; for example for version 16:

/usr/lib/jvm/jdk-16.0.2/bin/java -version
/usr/lib/jvm/jdk-16.0.2/bin/javac -version

- Install the new version trough update-alternatives in order to be able to switch between versions

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-20.0.2/bin/java 2011
sudo update-alternatives --config java

sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-20.0.2/bin/javac 2011
sudo update-alternatives --config javac




----- 16 -
/usr/lib/jvm/jdk-16.0.2/bin/java -version
/usr/lib/jvm/jdk-16.0.2/bin/javac -version

----- 15 -
/usr/lib/jvm/jdk-15.0.2/bin/java -version
/usr/lib/jvm/jdk-15.0.2/bin/javac -version

----- 14 -
/usr/lib/jvm/jdk-14.0.2/bin/java -version
/usr/lib/jvm/jdk-14.0.2/bin/javac -version

----- 13 -
/usr/lib/jvm/jdk-13.0.2/bin/java -version
/usr/lib/jvm/jdk-13.0.2/bin/javac -version

----- 12 -
/usr/lib/jvm/jdk-12.0.2/bin/java -version
/usr/lib/jvm/jdk-12.0.2/bin/javac -version

----- 10 -
/usr/lib/jvm/jdk-10.0.2/bin/java -version
/usr/lib/jvm/jdk-10.0.2/bin/javac -version

----- 9 -
/usr/lib/jvm/jdk-9.0.4/bin/java -version
/usr/lib/jvm/jdk-9.0.4/bin/javac -version


sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-16.0.2/bin/java 1611
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-16.0.2/bin/javac 1611

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-15.0.2/bin/java 1511
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-15.0.2/bin/javac 1511

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-14.0.2/bin/java 1411
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-14.0.2/bin/javac 1411

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-13.0.2/bin/java 1311
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-13.0.2/bin/javac 1311

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-12.0.2/bin/java 1211
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-12.0.2/bin/javac 1211

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-10.0.2/bin/java 1101
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-10.0.2/bin/javac 1101

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-9.0.4/bin/java 1091
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-9.0.4/bin/javac 1091