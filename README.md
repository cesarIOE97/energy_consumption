# Evolving Trends in Software Performance and Energy Consumption: An Analysis of Compilers and Interpreters over Time

## Abstract
Nowadays, society is concerned about climate change and the substantial energy demand for software applications generated in devices. This thesis analyzes the trends and impact of the interpreters and compilers of the most common programming languages, such as Python, C++, JavaScript, and Java, on software performance and energy consumption through their released versions.

This research analyzes how the selection of compiler or interpreter versions has impacted efficiency and how the trend of compilers and interpreters has been addressed in the last ten years. The results reveal that Python and JavaScript are highly sensitive to version changes, while Java shows robustness. Besides, we observe reduced energy consumption with newer Python versions, stabilization in Java and C++, and variation over time in JavaScript, but there is a gradual stabilization in the recently release versions. The study suggests that strategic version selection and optimization can lead to more energy-efficient software, thus addressing environmental concerns and performance demands.

## Introduction

### Motivation

 - Concern about the energy consumption of application software due to the impact of climate change
 - Software applications lead the computer system (hardware) in executing specific tasks which require considerable hardware resources to execute them affecting directly to the energy consumption
 - The demand for software applications and devices has increased significantly in the last few years
  
### Problem statement

 - Understand the root causes of the decreasing software performance observed nowadays and identify how impact energy consumption
 - Observe the trends and changes over time in the most common programming languages.
 - Identify the released versions that favourably impact energy consumption and performance.

### Research questions

 1. How is the trend of compiler and interpreter in the most common programming languages in terms of energy consumption and performance over time?
 2. How is the impact of selecting a specific compiler or interpreter version in the most common programming languages regarding energy consumption and performance?

## General characteristics

In order to answer the questions, the methodology consists of measuring the energy consumption and performance of different compiler and interpreter versions based on the selected programming languages. In addition, there are two specific programs to run in each programming language: one with a high demand for CPU usage and the other with a high demand for memory usage.

### Programming languages

Programming Language | Interpreter/Compiler | The oldest version | The newest version | Years
-------------|---------|-----------------|---------------|-------
 Python | CPython  | 2.5.6 | 3.11.3 | 2011 - 2023 (12 years)
 C++ | g++ | 4.4 | 13 | 2018 - 2023 (11 years)
 Java | javac | 1.8.0_382 | 20.0.2 | 2014* - 2023 (9 years)
 JavaScript | node | 0.8.28 | 20.5.1 | 2014 - 2023 (9 years)

*The First release of Java 8 is considered since its support is up to December 2026 by Oracle and the last release
date was on July 18, 2023.

### Programs

The Computer Language Benchmarks Game (CLBG) is a repository with different benchmark programs to compare the performance of different programming languages such as Python, C++, JavaScript, Java, and others. By selecting Binary-trees and N-body programs, the study analyzes their impact of energy consumption and software performance: one with a high demand for memory resources and the other with a high demand for processing to address the associated challenges.

### Set-up

 - Laptop Dell Inc. Latitude 7400 (Ubuntu 22.04.2 LTS 64-bit)
 - Memory 16 GB
 - Intel Core i5-8365U CPU @ 1.60 GHz x 8
 - Disk Capacity 512.1 GB

### Measurement software

- Energy measurement: Turbostat using Intel RAPL
  - Energy consumption of Package Processor (includes the cores and integrated graphics)
  - Energy consumption of RAM
  - Time elapased
- Performance measurement: Perf

## Measurement system

Figure shows the flowchart explaining the process of all measurement systems for assessing the performance of the selected program either Binary-trees or N-body with its respective scenario by running a Bash script in order to measure its performance in the programming languages.

The process starts by displaying all available languages (Python, C++, JavaScript, Java) and proceeds to the selection of one by the user. The respective versions of the compiler or interpreter (CPython,g++, Node, JavaC) are shown depending on the choice.

Then, the user can select testing all versions installed or a specific version, and the measurement system generates the commands needed to select the compiler or interpreter version and execute the programming language to test. Thus, Turbostat and perf measure the energy consumption and performance of every execution which is repeated ten times for accuracy before changing to the next compiler or interpreter version or, in case of testing the latest version from the list, ending with the measurements.

The results are compiled into an interactive HTML report for individual programs and updated in a general report that includes all the scenarios measured for analysis, concluding the process.

![Measurement System](measurement_system.jpg "Measurement System")

## Reference

[https://aaltodoc.aalto.fi/server/api/core/bitstreams/084ca7dd-6179-4ec4-9856-be80974e6945/content](https://aaltodoc.aalto.fi/server/api/core/bitstreams/084ca7dd-6179-4ec4-9856-be80974e6945/content)