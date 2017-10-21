# remoTeX
Short python script for remote compilation of LaTeX documents.

## Testing environment
### Client
* Ubuntu 14.04
	- Python 2.7.6 (or 3.4.3)
	- OpenSSH
	- rsync
	- scp

### Server
* CentOS 6.8
	- e-upTeX 3.14159265 (TeX Live 2016)
	- Latexmk 4.52
	- OpenSSH
	- rsync

## Preparation
### Client
* Setup your ssh with rsa-key and add your server setting to `~/.ssh/config`.
```
Host your-server
	HostName your.server.com
	Port 22
	user your-user-name
	IdentityFile ~/.ssh/id_rsa
```

### Server
* Add your client's id_rsa.pub to server's `~/.ssh/authorized_keys`.
* Install LaTeX on your server.
* Edit your server's `~/.latexmkrc`.
```
#!/usr/bin/env perl
$latex = 'uplatex %O %S';
$dvipdf = 'dvipdfmx %O %S';
$max_repeat = 5;
$pdf_mode = 3;	# use dvipdf
```

## Configuration
Edit your config file of remoTeX `remotex/config.py`.
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
host = 'your-server-host-name'
server_workdir = '~/documents'	# example
```

## Install
```
mkdir -p ~/local/src
git clone https://github.com/tankenta/remotex.git ~/local/src/
chmod +x ~/local/src/remotex/remotex.py
mkdir -p ~/local/bin
ln -s /home/your-use-name/local/src/remotex/remotex.py ~/local/bin/remotex
export PATH="$PATH:~/local/bin"
```

## Usage
```
remotex /path/to/your/project/directory
```
or
```
cd /path/to/your/project/directory
remotex
```
