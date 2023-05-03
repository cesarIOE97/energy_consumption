# Testing

## Programming Language

- [Testing](#testing)
  - [Programming Language](#programming-language)
    - [Python](#python)
      - [Basic](#basic)
      - [Compilers/Interpreters](#compilersinterpreters)
        - [CPython](#cpython)
        - [CODON](#codon)
    - [C++](#c)
      - [Basic](#basic-1)
      - [Compilers](#compilers)


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

Compilers | Version | Release date    | First release
----------|---------|-----------------|---------
 CPython | 3.11.3  | 2023-04-05 | 2022-10-24
 CPython | 3.10.11 | 2023-04-05 | 2021-10-04
 CPython | 3.9.16  | 2022-12-06 | 2020-10-05



_Sources:_
- [Python interpreters - Microsoft](https://learn.microsoft.com/en-us/visualstudio/python/installing-python-interpreters?view=vs-2022)


</details>

<details>
<summary>2. Java</summary>


</details>




<details>
<summary>3. JavaScript</summary>


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

[GCC](https://gcc.gnu.org/)

> The GNU Compiler Collection includes front ends for **C, C++, Objective-C, Fortran, Ada, Go, and D**, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's freedom.


Compilers | Version | Year
---------|----------|---------
 gcc | v11.3 | 2022-04-21
 gcc | v13.1 | 2023-04-26
  |  | 

[CLANG](https://clang.llvm.org/index.html)

> The Clang project provides a language front-end and tooling infrastructure for languages in the C language family (**C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript**) for the LLVM project. Both a GCC-compatible compiler driver (clang) and an MSVC-compatible compiler driver (clang-cl.exe) are provided. You can get and build the source today.

</details>


<details>
<summary>5. Go</summary>


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