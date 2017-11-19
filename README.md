# kafka-httpserver
python 封装的kafka http接口，方便一些没有kafka驱动的程序调用。

# 使用方法：
## 环境部署

```
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum install -y epel-release 
yum install -y python-pip gcc python-devel
pip install --upgrade pip
pip install Flask kafka-python supervisor gunicorn meinheld -i https://pypi.douban.com/simple
```

## 运行
### 使用 supervisor 运行
#### 1、如下配置 /etc/supervisord.conf
```
[supervisord]
nodaemon=true
 
[program:httpserver]
command=/usr/bin/gunicorn --chdir=/data/httpserver -c /data/httpserver/config.py server:app
```
#### 2、启动
/usr/bin/supervisord

### 直接启动
```gunicorn -c config.py server:app```

如果是存放在某个目录，比如 /data/httpserver ，可以实行如下命令启动：
```gunicorn --chdir=/data/httpserver -c /data/httpserver/config.py server:app```

## 测试
### 上报
```curl -d {"test":"now"} http://xxx.xxx.xxx.xxx:5000/<topic>```
Ps：接口自动使用一级目录作为kafka的topic。

### 查看
```
/patch_of_kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic <topic>  --from-beginning
```
