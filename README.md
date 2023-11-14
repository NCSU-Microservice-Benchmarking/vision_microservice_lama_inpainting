# Vision Microservice Lama Inpainting
Deploys [simple-lama-inpainting](https://github.com/enesmsahin/simple-lama-inpainting) as a microservice. The microservice uses an `Ubuntu 20.04.6 LTS` container (see below for more system information).


## Requirements

Luckily, base Ubuntu 20.04 has all that's needed. The remaining requirements are Python packages. [venv](https://docs.python.org/3/library/venv.html) is used to avoid cluttering the system (optional).

If you do not have the `venv` package, it is recommended to install it through the system package manager:
```console
# apt install python3.8-venv
```

Note: If you use `simple_lama` and run into the following error, you may need to `apt install libgl1`.
```console
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```


## Server Deployment

### Helper Script

```console
$ ./deploy.sh
```

### Manual

1. Create and activate the `venv` (optional)
```console
$ python3 -m venv .venv
$ source .venv/bin/activate # for bash/zsh
```

2. Install the required packages
```console
$ pip install simple-lama-inpainting
```

3. Start the [Flask](https://palletsprojects.com/p/flask) server:
```
$ flask run
```

## Testing

After deploying the server, `./send_request.py` sends `test_im.png` and `test_mask.png` in the current directory to the server. The result will be saved as `result.png`.

Note: `send_request.py` assumes the hostname is `http://127.0.0.1:5000`. Make sure to modify `host` if needed.

## System info
```console
(.venv) osalbahr@12841f99a914:~$ fastfetch 
                            ....    
              .',:clooo:  .:looooo:.    
           .;looooooooc  .oooooooooo'    
        .;looooool:,''.  :ooooooooooc    
       ;looool;.         'oooooooooo,    
      ;clool'             .cooooooc.  ,,    
         ...                ......  .:oo,    
  .;clol:,.                        .loooo'     osalbahr@12841f99a914
 :ooooooooo,                        'ooool     ---------------------
'ooooooooooo.                        loooo.    OS: Ubuntu focal 20.04 x86_64
'ooooooooool                         coooo.    Host: Alienware Aurora R9 (1.0.7)
 ,loooooooc.                        .loooo.    Kernel: 6.2.0-34-generic
   .,;;;'.                          ;ooooc     Uptime: 33 days, 6 hours, 32 mins
       ...                         ,ooool.     Packages: 358 (dpkg), 33 (brew)
    .cooooc.              ..',,'.  .cooo.      Shell: bash 5.0.17
      ;ooooo:.           ;oooooooc.  :l.       Terminal: node
       .coooooc,..      coooooooooo.           CPU: Intel(R) Core(TM) i9-9900K (16) @ 5.00 GHz
         .:ooooooolc:. .ooooooooooo'           Memory: 24.37 GiB / 62.61 GiB (39%)
           .':loooooo;  ,oooooooooc            Disk (/): 200.92 GiB / 1.83 TiB (11%) - overlay
               ..';::c'  .;loooo:'             Locale: en_US.UTF-8
                             .
                                               ████████████████████████
                                               ████████████████████████





(.venv) osalbahr@12841f99a914:~$ nvidia-smi 
Tue Nov 14 01:06:38 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.113.01             Driver Version: 535.113.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 2080 ...    Off | 00000000:01:00.0 Off |                  N/A |
| 18%   29C    P8              16W / 250W |     15MiB /  8192MiB |      0%      Default |
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
