#!/bin/bash

time="duration_time"
energy="power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/"
cpu="instructions,cycles,cpu-clock,context-switches,cpu-migrations,bus-cycles,cpu/branch-instructions/,C2_Pkg_Residency"
memory="cache-references,cache-misses,mem-loads,mem-stores,page-faults"
extra="msr/cpu_thermal_margin/"
all="duration_time,L1-dcache-load-misses,L1-dcache-loads,L1-dcache-stores,L1-icache-load-misses,LLC-load-misses,LLC-loads,LLC-store-misses,LLC-stores,branch-load-misses,branch-loads,dTLB-load-misses,dTLB-loads,dTLB-store-misses,dTLB-stores,iTLB-load-misses,iTLB-loads,node-load-misses,node-loads,node-store-misses,node-stores,branch-instructions,branch-misses,bus-cycles,cache-misses,cache-references,cpu-cycles,instructions,mem-loads,mem-stores,ref-cycles,topdown-fetch-bubbles,topdown-recovery-bubbles,topdown-slots-issued,topdown-slots-retired,topdown-total-slots,cstate_core/c3-residency/,cstate_core/c6-residency/,cstate_core/c7-residency/,cstate_pkg/c10-residency/,cstate_pkg/c2-residency/,cstate_pkg/c3-residency/,cstate_pkg/c6-residency/,cstate_pkg/c7-residency/,cstate_pkg/c8-residency/,cstate_pkg/c9-residency/,i915/actual-frequency/,i915/bcs0-busy/,i915/bcs0-sema/,i915/bcs0-wait/,i915/interrupts/,i915/rc6-residency/,i915/rcs0-busy/,i915/rcs0-sema/,i915/rcs0-wait/,i915/requested-frequency/,i915/software-gt-awake-time/,i915/vcs0-busy/,i915/vcs0-sema/,i915/vcs0-wait/,i915/vecs0-busy/,i915/vecs0-sema/,i915/vecs0-wait/,intel_bts//,intel_pt//,msr/aperf/,msr/cpu_thermal_margin/,msr/mperf/,msr/pperf/,msr/smi/,msr/tsc/,power/energy-cores/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/,power/energy-ram/"

metrics="CLKS,CORE_CLKS"



sudo perf stat -a -M $metrics -e $energy python3 nbody.py 50000



# Events for performance counters in Linux:

#  - duration_time  

# FOR CPU:
#  - cpu-cycles       These events count the number of CPU cycles executed which can help to measure the
#                     total number of instructions executed and provides insights into the overall CPU
#                     workload and identify performance bottlenecks

#  - instructions     Number of instructions executed gives an indication of the overall workload 
#                     of the processor to understand the complexity of the code being executed and
#                     can be used to compare and can help identify bottlenecks and areas for optimization

#  - cycles           NUmber of CPU cycles provides insight into the actual time taken by the processor
#                     to execute the code 

#  - cpu-clock        Measuring the CPU clock time provides an overall view of the time taken by the CPU 
#                     to execute a program. It accounts for both busy and idle times, giving an understanding
#                     of the total time spent by the CPU on the task

#  - context-switches Context switches occur when the OS switches the CPU from one task to another. Counting
#                     context switches helps evaluate the scheduling efficiency and multitasking behavior of
#                     system. High context switch rates can indicate suboptimal task scheduling or resource
#                     contention

#  - cpu-migrations   CPU migrations occur when a task is moved from one CPU core to another. Monitoring CPU
#                     migrations helps assess load balancing and CPU utilization across cores. High CPU 
#                     migration rates may suggest imbalanced workloads or suboptimal task scheduling

#  - bus-cycles       
#  - cache-references
#  - cache-misses
#  - branch-instructions
#  - branch-misses
#  - L1-dcache-loads
#  - L1-dcache-loads-misses
#  - L1-dcache-stores
#  - L1-dcache-stores-misses
#  - L1-icache-loads
#  - L1-icache-load-missed
#  - TLB-load-misses
#  - iTLB-load-misses
#  - LLC-loads
#  - LLC-load-misses
#  - LLC-stores
#  - LLC-store-misses
