---
title: "Docker in Local OS"
collection: teaching
type: "Bootcamp"
permalink: /teaching/002-bigdata-bootcamp-docker
venue: "Georgia Tech, School of CSE"
date: 2022-02-26
location: "Atlanta, GA"
toc: true
show: true
---

{% include user_def %}

> Reference: [[original website](http://chaozhang.org/bigdata-bootcamp/docs/environment/env-local-docker/)]

{{ hint_info }}
For the purpose of the environment normalization, we provide a simple [docker](https://docs.docker.com/) image for you, which contains most of the software required by this course. We also provide a few scripts to install some optional packages.
{{ _hint }}

The whole progress would seem as follow:

1. **Make sure you have enough resources**:
    - It requires at least 8GB of Physical RAM; 16GB or larger would be better
    - It requires at least 15GB of hard disk storage
2. Install a docker environment in the local machine
3. Start Docker Service, pull images, and create an instance
4. Just rock it!
5. Destroy the containers and images if they are no longer needed

{{ hint_warning }}
Since this docker image integrated many related services for the course, it requires at least 4GB RAM for this virtual machine.
If you can not meet the minimum requirement, the system could randomly kill one or a few processes due to resource limitation, which causes a lot of strange errors which is even unable to reproduce.

**DO NOT TRY TO DO THAT.**  
Instead, you can use cloud platforms such as [Azure](https://azure.microsoft.com/en-us/).
{{ _hint }}

## 0. System requirements

You should have enough system resources if you plan to start a container in your local OS.

You need to reserve at least 4 GB RAM for Docker and some extra memory for the host machine.
However, you can still start all the Hadoop-related services except [Zeppelin](https://zeppelin.apache.org), even if you only reserve 4GB for the virtual machine.

## 1. Install Docker

Docker is a software providing operating-system-level virtualization, also known as containers, promoted by the company [Docker, Inc.](docker.com).
Docker uses the resource isolation features of the Linux kernel such as cgroups and kernel namespaces, and a union-capable file system such as OverlayFS and others to allow independent "containers" to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines (VMs).
(from [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software)))
Basically, you can treat docker as a lightweight virtual machine with pretty high performance.

The installation instructions for different operating systems are provided in the links below.
You can also check the official documentation [here](https://docs.docker.com/engine/installation/) to get the latest news and detailed explanations.

+ [Install Docker In Linux](/teaching/0022-docker-linux)
+ [Install Docker In macOS](/teaching/0023-docker-macos)
+ [Install Docker In Microsoft Windows](/teaching/0021-docker-windows)

Once the docker is installed, you can start your docker services and launch your docker container using the following commands:

```bash
docker  # a tool to control docker
docker-machine  # a tool that lets you install Docker Engine on virtual hosts and manage the hosts in remote
docker-compose  # a tool for defining and running multi-container Docker applications
```

If we use VirtualBox + Windows/macOS, the theory is pretty clear: we created a Linux instance in "virtual remote", and control it using docker-machine.
If we want to operate the "remote docker service", we need to prepare a set of environment variables so that we do not have to use the `eval $(docker-machine env default)` command to access its location every time.
We can list it using the command:

```bash
docker-machine env default
```

{{ hint_warning }}
Command `docker-machine` has been removed from the later versions of Docker Desktop.
If you still want to use the command, you can follow the directions [here](https://stackoverflow.com/questions/60078434/docker-machine-command-not-found) and manually install the corresponding packages.

However, we will not rely on this command in our tutorial and its installation is *not required*.
{{ _hint }}

{{ hint_info }}
If you are using docker-machine, you cannot reach the port from virtual machine using ip address `127.0.0.1` (`localhost`).
As an alternative, you can extract the IP using this command:  
```bash
$ printenv  | grep "DOCKER_HOST"
DOCKER_HOST=tcp://192.168.99.100:2376
```
And visit `192.168.99.100` instead of `127.0.0.1` to access the network stream from the virtual machine.
{{ _hint }}

If these environments are not settled, docker will try to connect to the default Unix socket file.
As a Docker.app user, the file is: 

``` bash
$ ls -alh /var/run/docker.sock
lrwxr-xr-x  1 root  daemon    55B Feb 10 19:09 /var/run/docker.sock -> /Users/yu/Library/Containers/com.docker.docker/Data/s60
$ ls -al /Users/yu/Library/Containers/com.docker.docker/Data/s60
srwxr-xr-x  1 yu  staff  0 Feb 10 19:09 /Users/yu/Library/Containers/com.docker.docker/Data/s60
```

As a Linux user, the location is slightly different:

```bash
$ ls -al /var/run/docker.sock
srw-rw---- 1 root root 0 Feb 11 11:35 /var/run/docker.sock
```

{{ hint_info }}
A Linux user **must** add a "sudo" before command `docker` since he has no access to `docker.sock` as an ordinary user.
{{ _hint }}


## 2. Run Docker image

### 2.1. Start the container

The command to start the container used in the following tutorials is:

```bash
docker run -it --privileged=true \
  --cap-add=SYS_ADMIN \
  -m 8192m -h bootcamp.local \
  --name bigbox -p 2222:22 -p 9530:9530 -p 8888:8888\
  -v /:/mnt/host \
  sunlab/bigbox:latest \
  /bin/bash
```
It may take a while for the system to download and extract the container.

In general, the syntax of `docker run` is 

```bash
docker run [options] image[:tag|@digest] [command] [args]
```

Below explains the options used above:

{{ hint_info }}
```bash
-p <host-port>:<vm-port>
```

This option is used to map the TCP port `vm-port` in the container to port `host-port` on the Docker host.
Currently, the ports are reserved to:
+ 8888 - Jupyter Notebook
+ 9530 - Zeppelin Notebook

Once you have started the Zeppelin service, this service will keep listening port `9530` in docker.
You will be able to visit this service using `http://127.0.0.1:9530` or `http://DOCKER_HOST_IP:9530`.
The remote IP depends on the Docker Service you are running, which is described above.
+ If you are using Linux or Docker.app in macOS, you can visit "localhost:9530", or other ports if you changed `host-port`
+ If you are using VirtualBox + macOS or Windows, you should get the Docker's IP first
{{ _hint }}

{{ hint_info }}
```bash
-v, --volume=[host-src:]container-dest[:<options>]
```

This option is used to mount a volume.
Currently, we are using `-v /:/mnt/host`.
In this case, we can visit the root of your file system for your host machine.
If you are using macOS, `/mnt/host/Users/<yourname>/` would be the `$HOME` of your MacBook.
If you are using Windows, you can reach your `C:` disk from `/mnt/host/c` in docker.

Variable `host-src` accepts absolute path only.
{{ _hint }}

{{ hint_info }}
```bash
-it
```
+ -i              : Keep STDIN open even if not attached
+ -t              : Allocate a pseudo-tty
{{ _hint }}

{{ hint_info }}
```bash
-h bootcamp.local
```

Once you enter this docker environment, you can ping this docker environment itself as `bootcamp.local`. This variable is used in some configuration files for Hadoop ecosystems.
{{ _hint }}

{{ hint_info }}

```bash
-m 8192m
```

Memory limit (format: `<number>[<unit>]`).
The number should be a positive integer.
The unit can be one of `b`, `k`, `m`, or `g`.

This docker image requires at least 4G of RAM, while 8G is recommended when your physical machine has more than 8G of RAM.

The local machine is not the same as the remote server.
If you are launching a remote server with 8G RAM, you can set this number as 7G.
{{ _hint }}

Please refer to the [official documentation](https://docs.docker.com/engine/reference/run/) for more information and the detailed explanations.

### 2.2. Start all necessary services

{{ hint_info }}
In your terminal, you will generally meet two kinds of prompts.

```bash
[root@bootcamp /]# whoami  # this prompt '#' indices you are root aka the administrator of this environment now
root
[yu@bootcamp /]$ whoami  # this prompt '$' indices you are an ordinary user now
yu
```

You are in the `sudo` mode by default.
We also assume that you are always in the `sudo` mode in the following discussions.
{{ _hint }}

```bash
/scripts/start-services.sh
```

This script helps you to start the necessary services for the Hadoop ecosystems.

{{ hint_warning }}
You probably will encounter the "Connection Refused" exception if you forget to start these services.
{{ _hint }}

If you wish to host Zeppelin, you need to install it first by using the command:

```bash
/scripts/install-zeppelin.sh
```

And start the service with the command:

```bash
/scripts/start-zeppelin.sh
```

Then, Zeppelin will listen to the port `9530`.
Please refer to the [Zeppelin tutorial]({{base_path}}/teaching/003-bigdata-bootcamp-zeppelin) for more information about the configuration and usage of Zeppelin Notebook.


If you wish to host Jupyter, you can start it by using the command:

```bash
/scripts/start-jupyter.sh
```

Jupyter will listen to the port `8888`

### 2.3. Stop all services

You can stop the running services with:

```bash
/scripts/stop-services.sh
```


### 2.4. Detach or Exit

To detach and suspend a Docker instance from the terminal, use the command:

```bash
ctrl + p, ctrl + q
```

To exit,

```bash
exit
```

### 2.5. Re-attach

If you detached an instance and want to re-attach it, you need to check the `CONTAINER ID` or `NAMES` of it first.

```bash
$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND                CREATED             STATUS              PORTS                                                                  NAMES
011547e95ef5        sunlab/bigbox:latest   "/tini -- /bin/bash"   6 hours ago         Up 4 seconds        0.0.0.0:8888->8888/tcp, 0.0.0.0:9530->9530/tcp, 0.0.0.0:2222->22/tcp   bigbox
```

If the "STATUS" column is similar to "Exited (0) 10 hours ago", you can restart the container:

```bash
$ docker start <CONTAINER ID or NAMES>
```

And attach it with:

```bash
$ docker attach <CONTAINER ID or NAMES>
```

Every time you restart your container, you need to re-start the services (section 2.2) before any HDFS related operations.

### 2.6. Destroy instance

If you want to permanently remove the container:

```bash
$ docker rm <CONTAINER ID or NAMES>
```

### 2.7. Destroy images

If you want to permanently remove any images, you need to list images first:

```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
sunlab/bigbox       latest              bfd258e00de3        16 hours ago        2.65GB
```

And remove them by REPOSITORY or IMAGE ID using the command:

```bash
$ docker rmi <REPOSITORY or IMAGE ID>
```

### 2.8. Update images

```bash
$ docker pull sunlab/bigbox
```

### 2.9. Official documentations

Please refer to [this link](https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/) for the introduction of images, containers, and storage drivers.

### 2.10. Optional: use docker-compose

[Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container Docker applications.
A simple `docker-compose.yml` could *simplify* the parameters and make your life easier.

Please refer to [this page](/env/env-docker-compose.html#docker-compose) for further instructions.

## 3. Configurations and logs


### 3.1. System Configurations

```bash
$ cat /proc/meminfo  | grep Mem ## Current Memory
MemTotal:        8164680 kB ## Note: This value shoud no less than 4GB
MemFree:          175524 kB
MemAvailable:    5113340 kB
$ cat /proc/cpuinfo  | grep 'model name' | head -1  ## CPU Brand
model name	: Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz
$ cat /proc/cpuinfo  | grep 'model name' | wc -l ## CPU Count
4
$ df -h ## List Current Hard Disk Usage
Filesystem      Size  Used Avail Use% Mounted on
overlay          32G  4.6G   26G  16% /
tmpfs            64M     0   64M   0% /dev
...
$ ps -ef ## List Current Running Process
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 01:38 pts/0    00:00:00 /tini -- /bin/bash
root         7     1  0 01:38 pts/0    00:00:00 /bin/bash
root        77     1  0 01:43 ?        00:00:00 /usr/sbin/sshd
zookeep+   136     1  0 01:43 ?        00:00:14 /usr/lib/jvm/java-openjdk/bin/java -Dzookeeper.log.dir=/var/log/zookeeper -Dzookeeper.root.logger=INFO,ROLLINGFILE -cp /usr/lib/zookeeper/bin/../build/classes:/
yarn       225     1  0 01:43 ?        00:00:13 /usr/lib/jvm/java/bin/java -Dproc_proxyserver -Xmx1000m -Dhadoop.log.dir=/var/log/hadoop-yarn -Dyarn.log.dir=/var/log/hadoop-yarn -Dhadoop.log.file=yarn-yarn-pr
...
$ lsof -i:9530 ## Find the Process Listening to Some Specific Port
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
java    3165 zeppelin  189u  IPv4 229945      0t0  TCP *:9530 (LISTEN)
```

### 3.2. Logs

+ **hadoop-hdfs** -- /var/log/hadoop-hdfs/*
+ **hadoop-mapreduce**  -- /var/log/hadoop-mapreduce/*
+ **hadoop-yarn** -- /var/log/hadoop-yarn/*
+ **hbase**  --  /var/log/hbase/*
+ **hive**  -- /var/log/hive/*
+ **spark**  -- /var/log/spark/*
+ **zookeeper** -- /var/log/zookeeper/*
+ **zeppelin** -- /usr/local/zeppelin/logs/*
