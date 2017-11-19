#!/usr/bin/env python
# -*-coding:utf-8 -*-  
__author__ = "Jagerzhang"  
import multiprocessing  

# 绑定IP和端口
bind = '0.0.0.0:6666'  

preload_app = True  

# 进程数：本机cpu核数*2+1  
workers = multiprocessing.cpu_count() * 2 + 1

# 线程数
threads = multiprocessing.cpu_count() * 2  

# 允许挂起的连接数
backlog = 4096

# 工作模式为meinheld  
worker_class = "egg:meinheld#gunicorn_worker"

# debug开关
debug=False

# 守护模式（是否后台，如果使用supervisor来运行请设置为False）
daemon=True

proc_name = 'gunicorn.pid'  
pidfile = 'app_pid.log'  
loglevel = 'debug'  
logfile = 'debug.log'  
accesslog = 'access.log'  
access_log_format = '%(h)s %(t)s %(U)s %(q)s'  
