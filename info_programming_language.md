# Compiler and Interpreter versions

<details>
<summary>1. Python</summary>

## Python
Interpreters | Version | Release date    | First release | Status | Installation |
-------------|---------|-----------------|---------------|--------|--------------|
 CPython | 3.13.0a0  | 2023-06-07 | 2023-06-07 | alpha (preview) | installed
 CPython | 3.12.0b1  | 2023-05-22 | 2023-05-22 | beta (preview) | installed
 CPython | 3.11.3  | 2023-04-05 | 2022-10-24 | bugfix (suppported) | installed
 CPython | 3.10.11 | 2023-04-05 | 2021-10-04 | security (suppported) | installed
 CPython | 3.9.16 | 2022-12-06 | 2020-10-05 | security (suppported) | installed
 CPython | 3.8.16 | 2022-12-06 | 2019-10-14 | security (suppported) | installed
 CPython | 3.7.16 | 2022-12-06 | 2018-06-27 | security (suppported) | installed
 CPython | 3.6.15 | 2021-09-04 | 2016-12-23 | end-of-life (unsupported) | installed
 CPython | 3.5.10 | 2020-09-05 | 2015-09-13 | end-of-life (unsupported) | installed
 CPython | 3.4.10 | 2019-03-18 | 2014-03-16 | end-of-life (unsupported) | installed
 CPython | 3.3.7 | 2017-09-19 | 2012-09-29 | end-of-life (unsupported) | NO installed
 CPython | 3.2.6 | 2014-10-11 | 2011-02-20 | end-of-life (unsupported) | NO installed
 CPython | 3.1.5 | 2012-04-09 | 2009-06-27 | end-of-life (unsupported) | NO installed
 CPython | 3.0.1 | 2009-02-13 | 2008-12-03 | end-of-life (unsupported) | installed
 CPython | 2.7.18 | 2020-04-20 | 2010-07-04 | end-of-life (unsupported) | installed
 CPython | 2.6.9 | 2013-10-29 | 2008-10-01 | end-of-life (unsupported) | NO installed
 CPython | 2.5.6 | 2011-05-26 | 2006-09-19 | end-of-life (unsupported) | installed

Source:

 - [Status of Python Versions](https://devguide.python.org/versions/)
 - [Python Documentation by Version](https://www.python.org/doc/versions/)
 - [What's New in Python](https://docs.python.org/3/whatsnew/index.html)
 - [Development Cycle](https://devguide.python.org/developer-workflow/development-cycle/#devcycle)

</details>
<details>
<summary>2. Java</summary>

## Java

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
  ```
  sudo tar xvf ~/Downloads/openjdk-20.0.2_linux-x64_bin.tar.gz -C /usr/lib/jvm/
  ```
- Check the path for both java and javac by verifing their versions; for example for version 16:
  ```
  /usr/lib/jvm/jdk-16.0.2/bin/java -version
  /usr/lib/jvm/jdk-16.0.2/bin/javac -version
  ```
- Install the new version trough update-alternatives in order to be able to switch between versions
  ```
  sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-20.0.2/bin/java 2011
  sudo update-alternatives --config java

  sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-20.0.2/bin/javac 2011
  sudo update-alternatives --config javac 
  ```
- Source: 
  - https://kilishek.com/2021/05/05/installing-java-openjdk-from-tar-gz-archive-and-update-the-default-jdk-used/
  - https://www.java.com/releases/matrix/
  - https://www.java.com/releases/
  - https://jdk.java.net/archive/

</details>
<details>
<summary>3. JavaScript</summary>

## JavaScript

Compiler | Version | Release date    | First release | Status
---------|---------|-----------------|---------------|-------
 node | 20.5.1 | 2023-08-09	| 2023-04-18 | installed (current)
 node | 19.9.0 | 2023-04-10	| 2022-10-18 | installed (end of life)
 node | 18.17.1 | 2023-08-08 | 2022-04-19 | installed (active LTS)
 node | 17.9.1 | 2022-06-01 | 2021-10-19 | installed (end of life)
 node | 16.20.2 | 2023-08-08 | 2021-04-20 | installed (maintenance LTS)
 node | 15.14.0 | 2021-04-06 | 2020-10-20 | installed (end of life)
 node | 14.21.3 | 2023-02-16 | 2020-04-21 | installed (end of life LTS)
 node | 13.14.0 | 2020-04-29 | 	2019-10-22 | installed (end of life)
 node | 12.22.12 | 2022-04-05	| 2019-04-23 | installed (end of life LTS)
 node | 11.15.0 | 2019-04-30 | 2018-10-23 | installed (end of life)
 node | 10.24.1 | 2021-04-06 | 2018-04-24 | installed (end of life LTS)
 node | 9.11.2 | 2018-06-12 | 2017-10-01 | installed (end of life)
 node | 8.17.0 | 2019-12-17 | 2017-05-30 | installed (end of life LTS)
 node | 7.10.1 | 2017-07-11 | 2016-10-25 | installed (end of life)
 node | 6.17.1 | 2019-04-03	| 2016-04-26 | installed (end of life LTS)
 node | 5.12.0 | 2016-06-23	| 2015-10-29 | installed (end of life)
 node | 4.9.1 | 2018-03-29 | 2015-09-08 | installed (end of life LTS)
 node | 3.3.1 | 2015-09-15 | 2015-05-04 | installed (end of life)
 node | 2.5.0 | 2015-07-28 | 2015-05-04 | installed (end of life)
 node | 1.8.4 | 2015-07-09 | 2015-01-20 | installed (end of life)
 node | 0.12.18 | 2017-02-22	| 2015-02-06 | installed (end of life)
 node | 0.10.48 | 2016-10-18 | 2013-03-11 | installed (end of life)
 node | 0.8.28 | 2014-07-31	| 2012-06-25 | installed (end of life)


--Installation--
```
nvm install 16.20.2; nvm install 15.14.0; nvm install 14.21.3; nvm install 13.14.0; nvm install 12.22.12; nvm install 11.15.0; nvm install 10.24.1; nvm install 9.11.2; nvm install 8.17.0; nvm install 7.10.1; nvm install 6.17.1; nvm install 5.12.0; nvm install 4.9.1; nvm install 3.3.1; nvm install 2.5.0; nvm install 1.8.4; nvm install 0.12.18; nvm install 0.10.48; nvm install 0.8.28
```

</details>
<details>
<summary>4. C++</summary>

## C++

Compilers | Version | Release date    | First release | C+++ Standard Support | Status
------------|---------|-----------------|---------------|-------|------|
 GCC and G++ | 13.1 | 2023-04-26 | 2023-04-26 | C++23, C++20, C++17, C++14, C++11, C ++98 | installed
 GCC and G++ | 12.3 | 2023-05-08 | 2022-05-06 | C++23, C++20, C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 11.4 | 2023-05-29 | 2021-04-27 | C++23, C++20, C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 10.4 | 2022-06-28 | 2020-05-07 | C++20, C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 9.5 | 2022-05-27 | 2019-05-03 | C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 8.5 | 2021-05-14 | 2018-05-02 | C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 7.5 | 2019-11-14 | 2017-05-02 | C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 6.5 | 2018-10-26 | 2016-04-27 | C++17, C++14, C++11, C++98 | installed
 GCC and G++ | 5.5 | 2017-10-10 | 2015-04-22 | C++17,C++14, C++11, C++98 | installed
 GCC and G++ | 4.9.3 | 2015-06-26 | 2014-04-22 | C++14, C++11, C++98 | installed
 GCC and G++ | 4.8.5 | 2015-06-23 | 2013-03-22 | C++11, C++98 | installed
 GCC and G++ | 4.7.4 | 2014-06-12 | 2012-03-22 | C++11, C++98 | installed
 GCC and G++ | 4.6.4 | 2013-04-12 | 2011-03-25 | C++98 | installed
 GCC and G++ | 4.5.4 | 2012-07-02 | 2010-04-14 | C++98 | NO installed
 GCC and G++ | 4.4.7 | 2012-03-13 | 2009-10-15 | C++98 | installed
 GCC and G++ | 4.3.6 | 2011-06-27 | 2008-03-05 | C++23 | NO installed
 GCC and G++ | 4.2.4 | 2008-05-19 | 2007-05-13 | C++23 | NO installed
 GCC and G++ | 4.1.2 | 2007-02-13 | 2006-02-28 | C++23 | NO installed
 GCC and G++ | 4.0.4 | 2007-01-31 | 2005-04-20 | C++23 | NO installed
 GCC and G++ | 3.4.6 | 2006-03-06 | 2004-04-18 | C++23 | NO installed
 GCC and G++ | 3.3.6 | 2005-05-03 | 2003-05-13 | C++23 | NO installed
 GCC and G++ | 3.2.3 | 2003-04-22 | 2002-08-14 | C++23 | NO installed
 GCC and G++ | 3.0.4 | 2002-02-20 | 2001-01-18 | C++23 | NO installed (Configuration x86_64-unknown-linux-gnu not supported)

Command to verify the standars support in gcc compiler
```
g++-4.4 -v --help 2> /dev/null | sed -n '/^ *-std=\([^<][^ ]\+\).*/ {s//\1/p}'
```
Source:
 - [GCC Releases](https://gcc.gnu.org/releases.html)
 - [GCC Development Plan](https://gcc.gnu.org/develop.html)
 - [C++ Compiler Support](https://en.cppreference.com/w/cpp/compiler_support#References)


</details>




