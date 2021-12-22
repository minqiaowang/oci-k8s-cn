# Docker Container容器基础

## 简介

容器是打包代码及其所有依赖项的标准软件单元，因此应用程序可以从一个计算环境快速可靠地运行到另一个计算环境。 常用的容器运行时（container runtime）包括docker，containerd，rkt，katacontainer等等。容器镜像（image）是一个轻量级、独立、可执行的软件包，其中包括运行应用程序所需的一切：代码、运行时、系统工具、系统库和设置。容器镜像在运行时成为容器，以docker容器为例 - 镜像在 docker引擎上运行时成为容器。 可用于基于 Linux 和 Windows 的应用程序，无论基础架构如何，容器化软件始终是相同的运行。 容器将软件与其环境隔离开来，并确保它能够一致地工作。

![](images/image-20211221110624023.png)

### 实验目标

在本练习中，你将学会如何安装Docker环境，如何创建容器镜像，如何保存镜像到远程资料库，如何运行容器以及容器的管理等等。

### 先决条件

- 在OCI上创建一个VM，操作系统为Oracle Linux 7.9，机型选用缺省设置。
- 在hub.docker.com上注册一个账号，用来存储容器镜像。



## Task 1：安装配置Docker环境

1. 使用opc用户连接到所创建的Linux虚机。运行下列命令安装docker引擎。

    ```
    $ <copy>sudo yum -y install docker-engine</copy>
    ```

    

2. 授权opc用户使用docker命令

    ```
    $ <copy>sudo usermod -aG docker opc</copy>
    ```

    

3. 启动docker环境

    ```
    $ <copy>sudo systemctl enable docker</copy>
    $ <copy>sudo systemctl start docker</copy>
    ```



## Task 2: 运行你的第一个容器

1. 从远程资料库（缺省为hub.docker.com)中拉取一个容器镜像到本地。例如，我们可以拉取一个nginx容器镜像。

    ```
    $ <copy>docker pull nginx</copy>
    Using default tag: latest
    Trying to pull repository docker.io/library/nginx ... 
    latest: Pulling from docker.io/library/nginx
    a2abf6c4d29d: Pull complete 
    f3409a9a9e73: Pull complete 
    9919a6cbae9c: Pull complete 
    fc1ce43285d7: Pull complete 
    1f01ab499216: Pull complete 
    13cfaf79ff6d: Pull complete 
    Digest: sha256:366e9f1ddebdb844044c2fafd13b75271a9f620819370f8971220c2b330a9254
    Status: Downloaded newer image for nginx:latest
    nginx:latest
    ```

    

2. 查看当前镜像

    ```
    $ <copy>docker image ls</copy>
    REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    nginx               latest              f6987c8d6ed5        24 hours ago        141MB
    ```

    

3. 基于镜像启动容器。如果镜像不存在，docker会自动去远程资料库拉取镜像文件。

    ```
    $ <copy>docker run -d -it -p 80:80 --name my-nginx nginx</copy>
    d69ac4187f0da6bc41a9e3f8288e07d7a7c8545563f6322dc6ba3a5ca7da3fa1
    ```

    

4. 查看容器运行状态，该容器名字为`my-nginx`，本虚机的80端口映射到容器的80端口。

    ```
    $ <copy>docker ps -a</copy>
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
    d72bfc7ef659        nginx               "/docker-entrypoint.…"   16 seconds ago      Up 15 seconds       0.0.0.0:80->80/tcp   my-nginx
    ```

    

5. 我们可以连接进入该容器，缺省进入该容器根目录下。

    ```
    $ <copy>docker exec -it my-nginx bash</copy>
    root@9270794f6c08:/# 
    ```

    

6. 我们可以在容器内试着运行Linux命令。

    ```
    root@9270794f6c08:/# <copy>ls</copy>
    bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
    boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  usr
    root@9270794f6c08:/# 
    ```

    

7. 查看该容器的ip地址，可以看到该主机名就是CONTAINER ID。

    ```
    root@9270794f6c08:/# <copy>cat /etc/hosts</copy>
    127.0.0.1	localhost
    ::1	localhost ip6-localhost ip6-loopback
    fe00::0	ip6-localnet
    ff00::0	ip6-mcastprefix
    ff02::1	ip6-allnodes
    ff02::2	ip6-allrouters
    172.17.0.2	9270794f6c08
    root@9270794f6c08:/# 
    ```

    

8. 退出容器连接。

    ```
    root@9270794f6c08:/# <copy>exit</copy>
    exit
    $
    ```

    

9. 访问nginx容器80端口。使用刚才查询到的容器ip地址。

    ```
    $ <copy>curl http://172.17.0.2</copy>
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>
    
    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>
    
    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
    ```

    

10. 要让外部客户端访问虚机的80端口，我们必须先修改一下防火墙的设置。运行下列命令。

    ```
    $ <copy>sudo firewall-cmd --zone=public --add-port=80/tcp --permanent</copy>
    $ <copy>sudo firewall-cmd --reload</copy>
    ```

    

11. 另外，我们需要修改虚机所在的VCN公共子网的的安全规则，添加入站规则，允许访问80端口。

    ![image-20211222111541050](images/image-20211222111541050.png)

12. 打开浏览器，访问`http://<VM-publicIP>:80`，在运行容器时我们设置了端口映射，所以通过虚机的80端口可以访问到容器的nginx服务。

    ![image-20211222110342037](images/image-20211222110342037.png)

13. 停止该容器。

    ```
    $ <copy>docker stop my-nginx</copy>
    my-nginx
    ```

    

14. 删除该容器。

    ```
    $ docker rm my-nginx
    my-nginx
    ```

    

15. sdaf



## Task 3：创建一个自己的容器镜像

你可以从头开始创建容器镜像，也可以使用一个现有的镜像，在里面安装自己的应用。下面我们会从一个现有镜像alpine开始。Alpine是一个轻量级的Linux发行版，包含linux的核心组件。我们已经写好了一个python应用，该程序在每次调用时会随机加载一些图片。

1. sdfsdfa
2. sdaf
3. sadf
4. asdfsadf
5. sdaf
6. sadf
7. sdf
8. sdaf
9. 

