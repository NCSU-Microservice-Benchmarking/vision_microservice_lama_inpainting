# Vision Microservice Lama Inpainting
Deploys [simple-lama-inpainting](https://github.com/enesmsahin/simple-lama-inpainting) as a microservice, using ``.

## Environment setup

First, install [venv](https://docs.python.org/3/library/venv.html). I decided to do so through `apt`:
```console
# apt install python3.8-venv
```
Next, create the venv:
```console
$ python3 -m venv foo
```

Now you can activate the venv and install `simple-lama-inpainting`. In bash:
```console
$ source foo/bin/activate
$ pip install simple-lama-inpainting
```

## Runtime requirements

If you use `simple_lama` and run into the following error:
```console
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

you may need to `apt install libgl1`.

## System info
```console
(foo) osalbahr@12841f99a914:~$ fastfetch
                            ....               osalbahr@12841f99a914
              .',:clooo:  .:looooo:.           ---------------------
           .;looooooooc  .oooooooooo'          OS: Ubuntu focal 20.04 x86_64
        .;looooool:,''.  :ooooooooooc          Host: Alienware Aurora R9 (1.0.7)
       ;looool;.         'oooooooooo,          Kernel: 6.2.0-34-generic
      ;clool'             .cooooooc.  ,,       Uptime: 13 days, 8 hours, 38 mins
         ...                ......  .:oo,      Packages: 355 (dpkg), 13 (brew)
  .;clol:,.                        .loooo'     Shell: bash 5.0.17
 :ooooooooo,                        'ooool     Terminal: /dev/pts/0
'ooooooooooo.                        loooo.    CPU: Intel(R) Core(TM) i9-9900K (16) @ 5.00 GHz
'ooooooooool                         coooo.    Memory: 34.28 GiB / 62.61 GiB (55%)
 ,loooooooc.                        .loooo.    Disk (/): 110.56 GiB / 1.83 TiB (6%) - overlay
   .,;;;'.                          ;ooooc     Locale: C.UTF-8
       ...                         ,ooool.    
    .cooooc.              ..',,'.  .cooo.      ████████████████████████
      ;ooooo:.           ;oooooooc.  :l.       ████████████████████████
       .coooooc,..      coooooooooo.    
         .:ooooooolc:. .ooooooooooo'    
           .':loooooo;  ,oooooooooc    
               ..';::c'  .;loooo:'    
                             .
(foo) osalbahr@12841f99a914:~$ nvidia-smi 
Wed Oct 25 03:13:20 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.113.01             Driver Version: 535.113.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 2080 ...    Off | 00000000:01:00.0 Off |                  N/A |
| 18%   28C    P8              16W / 250W |     15MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce RTX 2080 ...    Off | 00000000:02:00.0 Off |                  N/A |
| 18%   28C    P8              13W / 250W |      6MiB /  8192MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
```
