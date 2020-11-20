# lmc-runner
Run LMC assembly code from the command line.

## Installation
Using **pip**:
```console
$ pip install lmc-runner
```

## Usage
### Help
```console
$ lmc-runner -h

lmc-runner [-h] name

positional arguments:
  name        LMC assembly code file name

optional arguments:
  -h, --help  show this help message and exit
```
### Run LMC file
```console
$ lmc-runner [name]
```
Example with an LMC assembly code file named `example.txt`
```console
$ lmc-runner example.txt
```


```
INP
STA 99
INP
ADD 99
STA 99
INP
ADD 99
OUT
HLT
```
