# Vision Microservice Lama Inpainting
Deploys [LaMa Image Inpainting](https://github.com/advimman/lama) as a microservice.

## Environment setup
I used the conda option in the upstream's [2. conda](https://github.com/advimman/lama#environment-setup).

## [Inference](https://github.com/advimman/lama#inference-)

Following the writeup:
```console
(lama) osalbahr@44e7b923309e:~/git/lama$ curl -L $(yadisk-direct https://disk.yandex.ru/d/xKQJZeVRk5vLlQ) -o LaMa_test_images.zip
Traceback (most recent call last):
  File "/home/osalbahr/miniconda3/envs/lama/bin/yadisk-direct", line 8, in <module>
    sys.exit(main())
  File "/home/osalbahr/miniconda3/envs/lama/lib/python3.6/site-packages/wldhx/yadisk_direct/main.py", line 23, in main
    print(*[get_real_direct_link(x) for x in args.sharing_link], sep=args.separator)
  File "/home/osalbahr/miniconda3/envs/lama/lib/python3.6/site-packages/wldhx/yadisk_direct/main.py", line 23, in <listcomp>
    print(*[get_real_direct_link(x) for x in args.sharing_link], sep=args.separator)
  File "/home/osalbahr/miniconda3/envs/lama/lib/python3.6/site-packages/wldhx/yadisk_direct/main.py", line 12, in get_real_direct_link
    return pk_request.json()['href']
KeyError: 'href'
curl: no URL specified!
curl: try 'curl --help' or 'curl --manual' for more information
```

This error was referenced in the following issue:

- [KeyError: 'href' occur When I use yadisk to download big-lama.zip #229](https://github.com/advimman/lama/issues/229)

It looks like the files are no longer available in https://disk.yandex.ru/d/xKQJZeVRk5vLlQ.

## System info
```console
(lama) osalbahr@44e7b923309e:~/git/lama$ fastfetch
                            ....               osalbahr@44e7b923309e
              .',:clooo:  .:looooo:.           ---------------------
           .;looooooooc  .oooooooooo'          OS: Ubuntu focal 20.04 x86_64
        .;looooool:,''.  :ooooooooooc          Host: Alienware Aurora R9 (1.0.7)
       ;looool;.         'oooooooooo,          Kernel: 6.2.0-34-generic
      ;clool'             .cooooooc.  ,,       Uptime: 13 days, 48 mins
         ...                ......  .:oo,      Packages: 315 (dpkg), 13 (brew)
  .;clol:,.                        .loooo'     Shell: bash 5.0.17
 :ooooooooo,                        'ooool     Terminal: /dev/pts/0
'ooooooooooo.                        loooo.    CPU: Intel(R) Core(TM) i9-9900K (16) @ 5.00 GHz
'ooooooooool                         coooo.    Memory: 34.04 GiB / 62.61 GiB (54%)
 ,loooooooc.                        .loooo.    Disk (/): 109.48 GiB / 1.83 TiB (6%) - overlay
   .,;;;'.                          ;ooooc     Locale: C.UTF-8
       ...                         ,ooool.    
    .cooooc.              ..',,'.  .cooo.      ████████████████████████
      ;ooooo:.           ;oooooooc.  :l.       ████████████████████████
       .coooooc,..      coooooooooo.    
         .:ooooooolc:. .ooooooooooo'    
           .':loooooo;  ,oooooooooc    
               ..';::c'  .;loooo:'    
                             .
```
