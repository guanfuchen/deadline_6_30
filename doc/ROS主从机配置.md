# ROS主从机配置

总共三台电脑，P3AT机器人主机，大疆无人机妙算主机，软件运行转载主机

[MultipleMachines](http://wiki.ros.org/ROS/Tutorials/MultipleMachines)

对于P3AT机器人主机和大疆无人机妙算主机，作为ROS从机，配置主机IP地址即可。

```
比如软件运行装载主机IP地址为192.168.31.171，那么这两台配置ROS主机地址如下
每一台机器上增加：export ROS_IP=`hostname -I`到bashrc中
主机配置：
roscore

# export ROS_MASTER_URI=http://localhost:11311
运行相关ros命令：如rosrun rospy_tutorials listener.py

从机配置
export ROS_MASTER_URI=http://192.168.31.171:11311
运行相关ros命令：如rosrun rospy_tutorials talker.py
```

对于软件运行装载主机，运行ROS即可。

```
roscore
```

# 测试通信正常与否

使用下述命令测试经过上述主从机配置后，通信是否正常。

```
主机
rosrun rospy_tutorials listener.py
从机
rosrun rospy_tutorials talker.py
两者调换顺序也可以
```
