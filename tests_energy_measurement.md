# Testing

## Measurement tool


<details>
<summary>RAPL on Linux (Perf)</summary>

### RAPL on Linux

#### **Description**

> Intel provides RAPL (Running Average Power Level) to provide estimated (and on some systems, actual) power measurements that the user can access. But how good are these measurements really? We set out to instrument some machines to find out. We looked primarily at the DRAM RAPL readings but also report a bit on the RAPL CPU and RAPL GPU measurements. In other words, it provides **estimated energy metrics for the CPU, integrated GPU and DRAM.**

There are four ways to read RAPL results on Linux, but the way used is through the `perf` command, which can be installed by the following commands.

```
sudo apt-get install linux-tools-5.15.0-71-generic
```

- To read RAPL result:
    ```
    sudo perf stat -a -e "power/energy-cores/" /bin/ls
    sudo perf stat -e power/energy-cores/,power/energy-ram/,power/energy-gpu/,power/energy-pkg/,power/energy-psys/ sleep 5
    sudo perf stat -r 5 -e power/energy-cores/ sleep 5 
    ```

    The second command helps to measure the energy consumption of a Linux built-in command, sleep for 5 seconds.
    The third command uses the `-r` command-line argument to specify how many times to measure the application

- Available events can be found via:
    ```
    perf list
    ```
    or
    ```
    ls /sys/bus/event_source/devices/power/events/
    ```

#### **RESULTS (ALL AVAILABLE EVENTS):**
```
olverac1@l20-0061:~$ ls /sys/bus/event_source/devices/power/events/
energy-cores        energy-gpu        energy-pkg        energy-psys        energy-ram
energy-cores.scale  energy-gpu.scale  energy-pkg.scale  energy-psys.scale  energy-ram.scale
energy-cores.unit   energy-gpu.unit   energy-pkg.unit   energy-psys.unit   energy-ram.unit
```
```
olverac1@l20-0061:~$ perf list

List of pre-defined events (to be used in -e):

  duration_time                                      [Tool event]

  branch-instructions OR cpu/branch-instructions/    [Kernel PMU event]
  branch-misses OR cpu/branch-misses/                [Kernel PMU event]
  bus-cycles OR cpu/bus-cycles/                      [Kernel PMU event]
  cache-misses OR cpu/cache-misses/                  [Kernel PMU event]
  cache-references OR cpu/cache-references/          [Kernel PMU event]
  cpu-cycles OR cpu/cpu-cycles/                      [Kernel PMU event]
  instructions OR cpu/instructions/                  [Kernel PMU event]
  mem-loads OR cpu/mem-loads/                        [Kernel PMU event]
  mem-stores OR cpu/mem-stores/                      [Kernel PMU event]
  ref-cycles OR cpu/ref-cycles/                      [Kernel PMU event]
  topdown-fetch-bubbles OR cpu/topdown-fetch-bubbles/ [Kernel PMU event]
  topdown-recovery-bubbles OR cpu/topdown-recovery-bubbles/ [Kernel PMU event]
  topdown-slots-issued OR cpu/topdown-slots-issued/  [Kernel PMU event]
  topdown-slots-retired OR cpu/topdown-slots-retired/ [Kernel PMU event]
  topdown-total-slots OR cpu/topdown-total-slots/    [Kernel PMU event]
  cstate_core/c3-residency/                          [Kernel PMU event]
  cstate_core/c6-residency/                          [Kernel PMU event]
  cstate_core/c7-residency/                          [Kernel PMU event]
  cstate_pkg/c10-residency/                          [Kernel PMU event]
  cstate_pkg/c2-residency/                           [Kernel PMU event]
  cstate_pkg/c3-residency/                           [Kernel PMU event]
  cstate_pkg/c6-residency/                           [Kernel PMU event]
  cstate_pkg/c7-residency/                           [Kernel PMU event]
  cstate_pkg/c8-residency/                           [Kernel PMU event]
  cstate_pkg/c9-residency/                           [Kernel PMU event]
  i915/actual-frequency/                             [Kernel PMU event]
  i915/bcs0-busy/                                    [Kernel PMU event]
  i915/bcs0-sema/                                    [Kernel PMU event]
  i915/bcs0-wait/                                    [Kernel PMU event]
  i915/interrupts/                                   [Kernel PMU event]
  i915/rc6-residency/                                [Kernel PMU event]
  i915/rcs0-busy/                                    [Kernel PMU event]
  i915/rcs0-sema/                                    [Kernel PMU event]
  i915/rcs0-wait/                                    [Kernel PMU event]
  i915/requested-frequency/                          [Kernel PMU event]
  i915/software-gt-awake-time/                       [Kernel PMU event]
  i915/vcs0-busy/                                    [Kernel PMU event]
  i915/vcs0-sema/                                    [Kernel PMU event]
  i915/vcs0-wait/                                    [Kernel PMU event]
  i915/vecs0-busy/                                   [Kernel PMU event]
  i915/vecs0-sema/                                   [Kernel PMU event]
  i915/vecs0-wait/                                   [Kernel PMU event]
  intel_bts//                                        [Kernel PMU event]
  intel_pt//                                         [Kernel PMU event]
  msr/aperf/                                         [Kernel PMU event]
  msr/cpu_thermal_margin/                            [Kernel PMU event]
  msr/mperf/                                         [Kernel PMU event]
  msr/pperf/                                         [Kernel PMU event]
  msr/smi/                                           [Kernel PMU event]
  msr/tsc/                                           [Kernel PMU event]
  power/energy-cores/                                [Kernel PMU event]
  power/energy-gpu/                                  [Kernel PMU event]
  power/energy-pkg/                                  [Kernel PMU event]
  power/energy-psys/                                 [Kernel PMU event]
  power/energy-ram/                                  [Kernel PMU event]
  uncore_cbox_0/clockticks/                          [Kernel PMU event]
  uncore_cbox_1/clockticks/                          [Kernel PMU event]
  uncore_cbox_2/clockticks/                          [Kernel PMU event]
  uncore_cbox_3/clockticks/                          [Kernel PMU event]
  uncore_imc/data_reads/                             [Kernel PMU event]
  uncore_imc/data_writes/                            [Kernel PMU event]
  uncore_imc/gt_requests/                            [Kernel PMU event]
  uncore_imc/ia_requests/                            [Kernel PMU event]
  uncore_imc/io_requests/                            [Kernel PMU event]
```




*Source*: 
- [RAPL](https://web.eece.maine.edu/~vweaver/projects/rapl/)
- [Chih's blog](https://blog.chih.me/read-cpu-power-with-RAPL.html)
- [Initial Validation of DRAM and GPU RAPL Power Measurements, 2015](https://web.eece.maine.edu/~vweaver/papers/tech_reports/2015_dram_rapl_tr.pdf)
- [Measuring energy](https://luiscruz.github.io/2021/07/20/measuring-energy.html)

#### **SCRIPT TO READ ALL POWER INFORMATION**



</details>


<details>
<summary>PowerTOP</summary>


</details>


<details>
<summary>PowerSTAT</summary>


</details>

<details>
<summary>likwid</summary>


</details>