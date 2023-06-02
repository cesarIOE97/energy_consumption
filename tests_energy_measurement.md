# Testing

- [Testing](#testing)
  - [Monitoring](#monitoring)
  - [Measurement tool](#measurement-tool)
    - [RAPL on Linux (Perf)](#rapl-on-linux-perf)
      - [**Description**](#description)
      - [**RESULTS (ALL AVAILABLE EVENTS):**](#results-all-available-events)
      - [**SCRIPT TO READ ALL POWER INFORMATION**](#script-to-read-all-power-information)
    - [PowerTOP](#powertop)
    - [PowerStat](#powerstat)
      - [**RESULTS (ALL AVAILABLE EVENTS):**](#results-all-available-events-1)
    - [Likwid](#likwid)
    - [Turbostat](#turbostat)
      - [Basic](#basic)
      - [Field descriptions](#field-descriptions)

## Monitoring



## Measurement tool


<details>
<summary>RAPL on Linux (Perf)</summary>

### RAPL on Linux (Perf)

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
    The list of options are as follows:

    ```
    -e, --event <event>   event selector. use 'perf list' to list available events
    -a, --all-cpus        system-wide collection from all CPUs
    -r, --repeat <n>      repeat command and print average + stddev (max: 100)
    ```
    1. The first command records the energy of the cores.
    2. The second command helps to measure the energy consumption of a Linux built-in command, sleep for 5 seconds.
    3. The third command uses the `-r` command-line argument to specify how many times to measure the application

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
- [DOCUMENTATION](https://perf.wiki.kernel.org/index.php/Tutorial)

#### **SCRIPT TO READ ALL POWER INFORMATION**



</details>


<details>
<summary>PowerTOP</summary>

### [PowerTOP](https://manpages.ubuntu.com/manpages/bionic/man8/powertop.8.html) 

> powertop  is  a  program  that helps to diagnose various issues with power consumption and
       power management.  It also has an interactive mode allowing one to experiment with various
       power  management  settings.   When invoking powertop without arguments powertop starts in
       interactive mode.

> It is a useful addition because it provides some additional information above and beyond what turbostat provides



_Source:_
- [GitHUB](https://github.com/fenrus75/powertop)

</details>


<details>
<summary>PowerSTAT</summary>

### [PowerStat](https://manpages.ubuntu.com/manpages/bionic/man8/powerstat.8.html)

> Powerstat was developed by Colin King and it is the simplest tool I have come across to measure energy consumption on Linux. 
>
> Powerstat  measures the power consumption of a computer that has a battery power source or
       supports the RAPL (Running Average Power Limit) interface.  The output is like vmstat  but
       also  shows  power  consumption statistics.  At the end of a run, powerstat will calculate
       the average, standard deviation, minimum, maximum and geometic mean of the gathered data.
> 
> **NOTE**: Provide only CPU energy consumption in Watts.

In order to install the tool:

```
sudo apt-get install -y powerstat
```

Basic commands:

```
sudo powerstat -R
powerstat 1 300
```

#### **RESULTS (ALL AVAILABLE EVENTS):**

```
olverac1@l20-0061:~/Desktop/thesis/energy_consumption$ sudo powerstat -R
[sudo] password for wa.olverac1: 
Running for 60.0 seconds (60 samples at 1.0 second intervals).
Power measurements will start in 0 seconds time.

  Time    User  Nice   Sys  Idle    IO  Run Ctxt/s  IRQ/s Fork Exec Exit  Watts
15:34:26   1.6   0.0   0.6  97.7   0.0    1    710    543    0    0    0   5.06 
15:34:27   0.9   0.0   0.4  98.6   0.1    1    967    558    1    0    1   5.05 
15:34:28   0.8   0.0   0.5  98.6   0.1    1    686    480    1    0    0   4.87 
15:34:29   0.8   0.0   0.4  98.9   0.0    1    596    367    0    0    0   4.91 
15:34:30   1.0   0.0   0.5  98.5   0.0    1    654    415    0    0    0   4.91 
15:34:31   0.5   0.0   0.4  99.1   0.0    1    532    366    0    0    0   4.79 
15:34:32   0.6   0.0   0.4  99.0   0.0    1    679    384    0    0    0   4.79 
15:34:33   0.9   0.0   0.4  98.5   0.3    1    799    533    1    0    1   5.27 
15:34:34   0.6   0.0   0.4  99.0   0.0    1    614    413    0    0    0   4.93 
15:34:35   0.6   0.0   0.3  99.1   0.0    1    647    397    0    0    0   4.76 
15:34:36   0.5   0.0   0.5  99.0   0.0    1    678    397    0    0    0   4.88 
15:34:37   0.8   0.0   0.3  99.0   0.0    2    596    409    0    0    0   4.83 
15:34:38   0.8   0.0   0.4  98.9   0.0    1    627    367    0    0    0   4.81 
15:34:39   1.0   0.0   0.6  98.2   0.1    1   1418    623    1    1    1   5.15 
15:34:40   0.5   0.0   0.3  99.2   0.0    5   1073    480    0    0    0   4.85 
15:34:41   1.3   0.0   0.5  98.1   0.1    1   1252    782    1    0    1   5.23 
15:34:42   0.5   0.0   0.4  99.1   0.0    1    683    442    0    0    0   4.80 
15:34:43   0.8   0.0   0.4  98.9   0.0    1    568    448    0    0    0   4.83 
15:34:44   0.6   0.0   0.3  99.0   0.1    2    632    397    0    0    0   4.87 
15:34:45   0.8   0.0   0.3  99.0   0.0    1    588    438    0    0    0   4.94 
15:34:46   0.8   0.0   0.3  98.9   0.1    1    632    414    0    0    0   5.00 
15:34:47   0.6   0.0   0.4  99.0   0.0    1    597    384    0    0    0   4.79 
15:34:48   6.8   0.0   2.5  89.8   0.9    1   8516   1808    8    0    0   9.08 
15:34:49   0.9   0.0   0.5  98.6   0.0    1    662    463    0    0    0   4.84 
15:34:50   0.8   0.0   0.5  98.7   0.0    1    794    373    0    0    0   4.82 
15:34:51   0.6   0.0   0.8  98.1   0.5    1   1279    569    3    0    3   5.05 
15:34:52   0.5   0.0   0.3  99.2   0.0    1    717    430    0    0    0   4.80 
15:34:53   0.9   0.0   0.4  98.7   0.0    1    621    357    0    0    0   4.78 
15:34:54   0.8   0.0   0.3  99.0   0.0    1    604    402    0    0    0   4.99 
15:34:55   0.6   0.0   0.4  99.0   0.0    1    695    458    0    0    1   4.84 
15:34:56   0.8   0.0   0.4  98.9   0.0    1    642    414    0    0    0   4.91 
15:34:57   0.8   0.0   0.4  98.9   0.0    1    666    426    0    0    1   4.82 
15:34:58   1.4   0.0   0.4  97.9   0.4    1    995    553    0    0    0   5.28 
  Time    User  Nice   Sys  Idle    IO  Run Ctxt/s  IRQ/s Fork Exec Exit  Watts
15:34:59   0.6   0.0   0.6  98.7   0.0    1    598    409    0    0    0   4.78 
15:35:00   0.6   0.0   0.3  99.1   0.0    1    711    472    0    0    0   4.85 
15:35:01   0.8   0.0   0.5  98.6   0.1    1    789    493    0    0    1   5.00 
15:35:02   1.9   0.0   0.5  97.5   0.1    1   1009    461    0    0    0   5.33 
15:35:03   1.6   0.0   0.9  97.4   0.1    1   1758    728    1    0    9   5.32 
15:35:04   0.4   0.0   0.3  99.4   0.0    1    605    406    0    0    0   4.79 
15:35:05   1.0   0.0   0.4  98.6   0.0    1   1126    453    0    0    0   4.88 
15:35:06   0.9   0.0   0.5  98.6   0.0    2    580    411    0    0    0   4.87 
15:35:07   0.4   0.0   0.1  99.5   0.0    1    619    439    0    0    0   4.80 
15:35:08   1.4   0.0   1.1  97.5   0.0    1   1155    555    0    0    0   5.19 
15:35:09   0.5   0.0   0.3  99.1   0.1    1    558    410    0    0    0   5.02 
15:35:10   1.0   0.0   0.1  98.9   0.0    1    654    381    0    0    0   4.85 
15:35:11   0.6   0.0   0.4  99.0   0.0    1    865    461    0    0    0   4.94 
15:35:12   0.5   0.0   0.3  99.2   0.0    1    659    430    0    0    0   4.84 
15:35:13   0.9   0.0   0.5  98.6   0.0    1    509    390    0    0    0   4.92 
15:35:14   0.9   0.0   0.3  98.9   0.0    1    577    358    0    0    0   4.85 
15:35:15   0.6   0.0   0.3  98.9   0.3    1    591    415    0    0    0   4.97 
15:35:16   0.6   0.0   0.1  99.2   0.0    1    565    372    0    0    0   4.78 
15:35:17   0.5   0.0   0.4  99.1   0.0    1    753    434    0    0    0   4.98 
15:35:18   1.1   0.0   0.4  97.9   0.6    1   1061    571    0    0    0   5.29 
15:35:19   0.5   0.0   0.5  99.0   0.0    1    511    394    0    0    0   4.77 
15:35:20   0.5   0.0   0.1  99.4   0.0    1    766    419    0    0    0   4.88 
15:35:21   0.9   0.0   0.4  98.7   0.0    2    573    387    0    0    0   4.85 
15:35:22   0.9   0.0   0.3  98.9   0.0    1    633    391    0    0    0   4.82 
15:35:23   0.5   0.0   0.4  99.1   0.0    1    631    402    0    0    0   4.84 
15:35:24   3.6   0.0   1.4  95.0   0.0    1   2060    739    0    0    0   5.31 
15:35:25   5.3   0.0   2.5  92.0   0.1    1   4659   1611    0    0    0   5.91 
-------- ----- ----- ----- ----- ----- ---- ------ ------ ---- ---- ---- ------ 
 Average   1.0   0.0   0.5  98.4   0.1  1.1  966.6  494.7  0.3  0.0  0.3   5.02 
 GeoMean   0.8   0.0   0.4  98.4   0.0  1.1  787.4  465.5  0.0  0.0  0.0   5.00 
  StdDev   1.1   0.0   0.4   1.6   0.2  0.6 1139.8  243.7  1.1  0.1  1.2   0.57 
-------- ----- ----- ----- ----- ----- ---- ------ ------ ---- ---- ---- ------ 
 Minimum   0.4   0.0   0.1  89.8   0.0  1.0  509.0  357.0  0.0  0.0  0.0   4.76 
 Maximum   6.8   0.0   2.5  99.5   0.9  5.0 8516.0 1808.0  8.0  1.0  9.0   9.08 
-------- ----- ----- ----- ----- ----- ---- ------ ------ ---- ---- ---- ------ 
Summary:
CPU:   5.02 Watts on average with standard deviation 0.57  
Note: power read from RAPL domains: package-0, uncore, package-0, dram, core, dram, psys.
These readings do not cover all the hardware in this device.

```

</details>

<details>
<summary>likwid</summary>

### Likwid

The following commands are to install:

```
git clone https://github.com/RRZE-HPC/likwid.git
cd likwid
make
sudo make install
```

Some examples using the command:

```
olverac1@l20-0061:~/Desktop/thesis/likwid$ likwid-powermeter sleep 15
--------------------------------------------------------------------------------
CPU name:	Intel(R) Core(TM) i5-8365U CPU @ 1.60GHz
CPU type:	Intel Kabylake processor
CPU clock:	1.90 GHz
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Runtime: 16.0891 s
Measure for socket 0 on CPU 0
Domain PKG:
Energy consumed: 33.4855 Joules
Power consumed: 2.08126 Watt
Domain PP0:
Energy consumed: 2.47858 Joules
Power consumed: 0.154054 Watt
Domain PP1:
Energy consumed: 0.0716553 Joules
Power consumed: 0.00445367 Watt
Domain DRAM:
Energy consumed: 5.04352 Joules
Power consumed: 0.313475 Watt
Domain PLATFORM:
Energy consumed: 151.709 Joules
Power consumed: 9.42933 Watt
--------------------------------------------------------------------------------

```



</details>



<details>
<summary>turbostat</summary>

### Turbostat

#### Basic 

Turbostat is a simple but powerful tool that is built into the Linux kernel tree. It monitors.

 - Per-thread: Average frequency, activity
 - Per-core: Core C-states, temperature
 - Per-package: Temperature, package C-states, package power, core power (where supported), DRAM power.

Turbostat has several different command-line options that can come in handy for a range of usage models. Simply running it without any parameters will provide one-second snapshots of a range of statistics.

Turbostat is very useful to run alongside a workload to get statistics about the system during the measurement. Note that although the statistics provided are heavily influenced by the workload, it is also affected by anything else running on the system.

INSTALL THE TOOL:

```bash
sudo apt install linux-tools-5.15.0-72-generic
```

OPTIONS
```bash
sudo turbostat -S
```


#### Field descriptions


</details>