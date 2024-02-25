# Python versions

Supported versions
 - 3.11 - 10-60% faster than Python 3.10
 - 3.10
 - 3.9
 - 3.8
 - 3.7

End-of-life (unsupported versions):
 - 3.6
 - 3.5
 - 3.4
 - 3.3
 - 3.2
 - 3.1
 - 3.0
 - 2.7
 - 2.6

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



Source:

 - [Status of Python Versions](https://devguide.python.org/versions/)
 - [Python Documentation by Version](https://www.python.org/doc/versions/)
 - [What's New in Python](https://docs.python.org/3/whatsnew/index.html)
 - [Development Cycle](https://devguide.python.org/developer-workflow/development-cycle/#devcycle)

## Pyenv

-What is pyenv?
  `pyenv` lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

Besides, `pyenv` lets to change the global Python version on a per-user basis, provide support for per-project Python versions, allows to override the Python version with an environment variable, and searches for commands from multiple versions of Python at a time,


- Advantages against `pythonbrew` and `pythonz`:
  - `pyenv` does not depend on Python itself since it was made from pure shell scripts. There is no bootstrap problem of Python
  - `pyenv` does not need to be loaded into your shell. Instead, pyenv's shim approach works by adding a directory to your `PATH`
  - `pyenv` does not manage virtualenv. Although, it is able to create `virtualenv` yourself, or `pyenv-virtualenv` to automate the process


- Some solutions during the installation

The next command is the solution to load the updated configuration file when a new session is started, eliminating the need to manually run 'exec "$SHELL"'. However, note that changes made to an existing session will still require a restart or the exec "$SHELL" command to take effect.
```
source "$HOME/.bashrc"  # or .zshrc for Zsh
```

Add the next lines in the `/etc/sudoers` using the command `sudo visudo`:
```
olverac1  ALL=(ALL) ALL
olverac1  ALL=(root) NOPASSWD: /u/13/olverac1/unix/Desktop/thesis/energy_consumption/measurement
olverac1  ALL=(ALL) NOPASSWD:ALL


olverac1 ALL=(ALL) NOPASSWD: ALL
olverac1 ALL=NOPASSWD: /u/13/olverac1/unix/Desktop/thesis/energy_consumption/measurement
```

Solution of the issue of SSL of the current versions
```
sudo apt install -y libssl-dev
```


- [Solution for /etc/sudoers](https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/)


# Extract relevant columns
python_version = df['python_version']
release = df['release_date']
first_release = df['first_release']
time_elapsed = df['time_elapsed']       # 
avg_mhz = df['Avg_MHz']                 # no. of cycles executed divided by time elapsed
busy_percent = df['Busy%']              # % of time in C0 state
busy_mhz = df['Bzy_MHz']                # Avg clock rate while the CPU was not idle in C0 state
ipc = df['IPC']                         # 
irq = df['IRQ']                         # (#) of interrupts serviced by that CPU during the measurement interval. The system total line is the sum of interrupts serviced across all CPUs
poll = df['POLL']                       # 
c1 = df['C1']                           # 
c1e = df['C1E']                         # 
c3 = df['C3']                           # 
c6 = df['C6']                           # 
c7s = df['C7s']                         # 
c8 = df['C8']                           # 
coreTemperature = df['CoreTmp']         # (ªC) by the per-core Digital Thermal Sensor
pkgTemperature = df['PkgTmp']           # (ªC) by the per-package Package Thermal Monitor
gfx_percent = df['GFX%rc6']             # Percentage of time the GPU is in the "render C6" state
gfx_mhz = df['GFXMHz']                  # 
total_c0_percent = df['Totl%C0']        # 
any_c0_percent = df['Any%C0']           # 
gfx_c0_percent = df['GFX%C0']           # 
cpugfx_percent = df['CPUGFX%']          # 
energy_pkg = df['Pkg_J']                # 
energy_core = df['Cor_J']               # 
energy_gfx = df['GFX_J']                # 
energy_ram = df['RAM_J']                # 




OPTIONS FOR ANALYSIS - PERF (DEEPER)

pyenv global <python_version>
sudo env "PATH=$PATH VIRTUAL_ENV=$VIRTUAL_ENV PYENV_ROOT=$PYENV_ROOT" perf record -a python <python_program>

sudo perf report -i perf_2.5.6.data
