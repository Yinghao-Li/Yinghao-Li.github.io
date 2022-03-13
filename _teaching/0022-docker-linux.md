---
title: "Install Docker in Linux"
collection: teaching
type: "Bootcamp"
permalink: /teaching/0022-docker-linux
venue: "Georgia Tech, School of CSE"
date: 2022-02-26
location: "Atlanta, GA"
toc: true
show: false
---

> Reference: [[original website](http://chaozhang.org/bigdata-bootcamp/docs/environment/env-local-docker-linux/), [official tutorial](https://docs.docker.com/engine/install/)]

## 1. Install Docker on RHEL/CentOS/Fedora

+ [Get Docker CE for CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
+ [Get Docker CE for Fedora](https://docs.docker.com/engine/installation/linux/docker-ce/fedora/)

In brief, you can install Docker and start the service with the following commands:

```bash
sudo yum install docker-ce -y  # install docker package
sudo service  docker start  # start docker service
chkconfig docker on  # start-up automatically
```

### FAQ

**If your SELinux and BTRFS are on working, you may meet an error message as follow:**

```bash
# systemctl status docker.service -l
...
SELinux is not supported with the BTRFS graph driver!
...
```

Modify /etc/sysconfig/docker as follow:

```bash
# Modify these options if you want to change the way the docker daemon runs
#OPTIONS='--selinux-enabled'
OPTIONS=''
...
```

Restart your docker service

**Storage Issue:**

Error message found in /var/log/upstart/docker.log

```
[graphdriver] using prior storage driver \"btrfs\"...
```

Just delete directory /var/lib/docker and restart the Docker service

## 2. Install Docker on Ubuntu/Debian

+ [Get Docker CE for Ubuntu](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
+ [Get Docker CE for Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)

Generally, you can add the repository and execute

```bash
sudo apt-get install docker-ce
```

Both Debian Series and RHEL Series can be controlled by

```bash
sudo service docker start # stop, restart, ...
```

Once you started your service, you would find a socket file `/var/run/docker.sock`, and then you are able to execute your docker commands.
