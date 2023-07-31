Compiler | Version | Release date    | First release | Status
---------|---------|-----------------|---------------|-------
 javac | 20.0.2 | 2023-07-18 | 2023-03-21 | installed
 javac | 19.0.2 | 2023-01-17 | 2022-09-20 | installed
 javac | 18.0.2-ea | 2022-07-19 | 2022-03-22 | installed
 javac | 17.0.7 | 2023-04-18 | 2021-09-14 | installed
 javac | 16.0.2 | 2021-07-20 | 2021-03-16 | installed
 javac | 15.0.2 | 2021-01-19 | 2020-09-15	 | installed
 javac | 14.0.2 | 2020-07-14 | 2020-03-17 | installed
 javac | 13.0.2 | 2020-01-14 | 2019-09-17 | installed
 javac | 12.0.2 | 2019-07-16 | 2019-03-19 | installed
 javac | 11.0.19 | 2020-10-20 | 2018-09-25 | installed
 javac | 10.0.2 | 2018-07-17 | 2018-03-20 | installed
 javac | 9.0.2 | 2018-01-16 | 2017-09-21 | installed
 javac | 1.8.0_362 | 2023-04-18 | 2014-03-18 | installed


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



- Source: 
  - https://kilishek.com/2021/05/05/installing-java-openjdk-from-tar-gz-archive-and-update-the-default-jdk-used/
  - https://www.java.com/releases/matrix/
  - https://www.java.com/releases/
  - https://jdk.java.net/archive/


