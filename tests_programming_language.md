# Testing

## Programming Language

- [Testing](#testing)
  - [Programming Language](#programming-language)
    - [Python](#python)
      - [Basic](#basic)
      - [Compilers/Interpreters](#compilersinterpreters)
        - [CPython](#cpython)
        - [CODON](#codon)
    - [Java](#java)
      - [Basic](#basic-1)
      - [Compilers/Interpreters](#compilersinterpreters-1)
        - [OpenJDK](#openjdk)
        - [](#)
      - [Basic](#basic-2)
      - [Compilers/Interpreters](#compilersinterpreters-2)
        - [Node.js](#nodejs)
    - [C++](#c)
      - [Basic](#basic-3)
      - [Compilers](#compilers)
        - [GCC](#gcc)
        - [CLANG](#clang)
    - [GO](#go)
      - [Basic](#basic-4)
      - [Compilers](#compilers-1)
        - [Go](#go-1)


<details>
<summary>1. Python</summary>

### Python

#### Basic

The basic commands to run a Python code.

```
touch helloWorld.py
python3 helloWorld.py
```
A simple Python code

```python
if __name__ == '__main__':
    
    print("Hello World! We're working on Python")
```

#### Compilers/Interpreters

##### [CPython](https://www.python.org/)

> 	The "native" and most commonly used interpreter, available in 32-bit and 64-bit versions (32-bit recommended). Includes the latest language features, maximum Python package compatibility, full debugging support, and interop with IPython.

##### [CODON](https://docs.exaloop.io/codon/)

> Codon is a high-performance Python compiler that **compiles Python code to native machine code without any runtime overhead**. Typical speedups over Python are on the order of 100x or more, on a single thread. Codon supports native multithreading which can lead to speedups many times higher still.
> 
> The Codon framework is fully modular and extensible, allowing for the seamless integration of new modules, compiler optimizations, domain-specific languages and so on. We actively develop Codon extensions for a number of domains such as bioinformatics and quantitative finance.
> The command to install is the next one:
> ```
> /bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)" 
> ```
>
> In order to run the command uses the next commands:
> ```
> echo 'export PATH=${HOME}/.codon/bin:${PATH}' >> ~/.bashrc
> exec $SHELL
> ```
> The codon compiler has a number of options and modes:
> ```
> # compile and run the program
> codon run fib.py
> # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
> 
> # compile and run the program with optimizations enabled
> codon run -release fib.py
> # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
> 
> # compile to executable with optimizations enabled
> codon build -release -exe fib.py
> ./fib
> # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
> 
> # compile to LLVM IR file with optimizations enabled
> codon build -release -llvm fib.py
> # outputs file fib.ll
> ```


**_Summary_**

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 CPython | 3.11.3  | 2023-04-05 | 2022-10-24
 CPython | 3.10.11 | 2023-04-05 | 2021-10-04
 CPython | 3.9.16  | 2022-12-06 | 2020-10-05
 CPython (Now) | 3.10.6 | 2022-08-02 | 2021-10-04
 Codon (Now) | 0.16.0 | 2023-04-17 | 2023-04-17
 Codon | 0.15.1 | 2022-12-05 | 2022-12-05



_Sources:_
- [Python interpreters - Microsoft](https://learn.microsoft.com/en-us/visualstudio/python/installing-python-interpreters?view=vs-2022)


</details>

<details>
<summary>2. Java</summary>

### Java

#### Basic

The basic commands to run a Java code.

```
javac helloWorld.java
java helloWorld
```
A simple Java code

```java
class HelloWorld
{
	// Your program begins with a call to main().
	// Prints "Hello, World" to the terminal window.
	public static void main(String args[])
	{
		System.out.println("Hello, World! We're working on Java");
	}
}

```
#### Compilers/Interpreters


##### [OpenJDK](https://openjdk.org/projects/jdk-updates/)



##### 

**_Summary_**

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 OpenJDK (now) | 11.0.18 | 2023-01-17 | 2018-10-01
 OpenJDK  | 9.0.4 | 2018-01-01 | 2017-10-01
 OracleJDK
 IBMJDK
 Azul Zulu



</details>




<details>
<summary>3. JavaScript</summary>

#### Basic

The basic commands to run a Java code.

```
javac helloWorld.java
java helloWorld
```
A simple Java code

```javascript
class HelloWorld
{
	// Your program begins with a call to main().
	// Prints "Hello, World" to the terminal window.
	public static void main(String args[])
	{
		System.out.println("Hello, World! We're working on JavaScript");
	}
}

```
#### Compilers/Interpreters


##### [Node.js](https://nodejs.org/en/download/releases)

> Node.js is an open-source runtime environment for the JavaScript language that reshapes JavaScript’s characteristics and upgrades its functionality. As a result, you can use JavaScript for frontend and backend development, enabling full-stack development solely using JavaScript.
> The commands to install is the next one:
> ```
> wget https://nodejs.org/dist/v20.1.0/node-v20.1.0-linux-x64.tar.xz
> wget https://nodejs.org/dist/v20.1.0/node-v20.1.0-linux-x64.tar.xz
> sudo cp -r node-v20.1.0-linux-x64/{bin,include,lib,share}  /usr/
> find /usr -name node
> node --version
> ```
> In order to run the code
> ```
> node helloWorld.js
> ```

**_Summary_**

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 node (now) | 20.1.0 | 2023-05-03 | 2023-04-18
 node (recommended)  | 18.16.0 LTS | 2023-04-12 | 2022-04-19

**Source:**

- [Install Node.js](https://www.golinuxcloud.com/install-nodejs-ubuntu-from-tar-xz/)
- [All releases](https://github.com/nodejs/node/blob/main/doc/changelogs/CHANGELOG_V18.md#18.0.0)

</details>




<details>
<summary>4. C++</summary>

### C++

#### Basic

The basic commands to run a C code.

```
touch helloWorld.c
chmod +x helloWorld.c
gcc helloWorld.c -o sample
./sample
```
A simple C++ code

```cpp
#include <stdio.h>

int main()
{
    printf("\nHello world! We're working on C++\n\n");
    return 0;
}
```

#### Compilers

##### [GCC](https://gcc.gnu.org/)

> The GNU Compiler Collection includes front ends for **C, C++, Objective-C, Fortran, Ada, Go, and D**, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's freedom.


##### [CLANG](https://clang.llvm.org/index.html)

> The Clang project provides a language front-end and tooling infrastructure for languages in the C language family (**C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript**) for the LLVM project. Both a GCC-compatible compiler driver (clang) and an MSVC-compatible compiler driver (clang-cl.exe) are provided. You can get and build the source today.

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 gcc (Now) | 11.3.0 | 2022-04-21 | 2021-04-27
 gcc | 13.1 | 2023-04-26 | 2023-04-26
 gcc | 10.4 | 2022-06-28 | 2020-05-07

</details>


<details>
<summary>5. Go</summary>

### GO

#### Basic

The basic commands to run a Go code.

```
go run helloWorld.go      // Run directly the code
go build helloWorld.go    // Build the program into binaries
./helloWorld
```
A simple Go code

```go
// First Go program
package main

import "fmt";

// Main function
func main() {

	fmt.Println("Hello World! We're working on Go")
}
```

#### Compilers

##### Go

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 go (Now) | 1.20.4 | 2023-05-02 | 2023-02-14

</details>



<details>
<summary>6. Rust</summary>


</details>

<details>
<summary>7. Ruby</summary>


</details>


<details>
<summary>8. R</summary>


</details>

<details>
<summary>9. C#</summary>


</details>

<details>
<summary>10. PHP</summary>


</details>

<details>
<summary>11. Swift</summary>


</details>

<details>
<summary>12. Kotlin</summary>


</details>

<details>
<summary>13. TypeScript</summary>


</details>