## 环境搭建

### 基础服务安装

#### 开启FTP服务

安装并配置

```sh
hzfy@ubuntu:~$ sudo apt-get install vsftpd

hzfy@ubuntu:~$ sudo vim /etc/vsftpd.conf 
```

编辑vsftpd.conf 开启本地用户登录和写权限，如下去掉注释

```sh
# Uncomment this to allow local users to log in.
local_enable=YES
#
# Uncomment this to enable any form of FTP write command.
write_enable=YES
```

重启FTP服务

```sh
hzfy@ubuntu:~$ sudo /etc/init.d/vsftpd restart
```

#### 开启NFS服务

安装并配置

```sh
sudo apt-get install nfs-kernel-server rpcbind
sudo vi /etc/exports

# 添加如下内容
/home/hzfy/nfs *(rw,sync,no_root_squash)

# 重启服务
sudo /etc/init.d/nfs-kernel-server restart
```

#### 开启SSH服务

安装并配置

```sh
sudo apt-get install openssh-server
```

### 安装交叉编译器

```sh
sudo cp gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz /usr/local/arm/ -f
sudo tar -vxf gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf.tar.xz
sudo vi /etc/profile
# 添加如下内容
export PATH=$PATH:/usr/local/arm/gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf/bin
```

#### 安装其他相关库

```sh
sudo apt-get update //先更新，否则安装库可能会出错
sudo apt-get install lsb-core lib32stdc++6 //安装库
```

#### 版本验证

查看版本号

```sh
arm-none-linux-gnueabihf-gcc -v
```