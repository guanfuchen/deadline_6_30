# P3AT机器人

- 硬件安装
- 安装系统（联想笔记本，Fn+F2进入bios）
- 安装ROS
- 安装ZED双目摄像头相应软件
- 安装rosaria（P3AT机器人底层控制软件）

## 硬件安装

ZED双目摄像头，串口，和笔记本电脑均通过USB连接，问题：笔记本安装过程中，电源接口无法充电（负责人：吴）

## 系统安装

ubuntu14.04配套ros indigo，P3AT机器人、大疆无人机和测试机均使用统一系统，安装同一版本的ROS（不同版本ROS之间的通信问题）。
用户名hpec，密码为笔记本上面写的原密码。

合上笔记本不睡眠。
```
sudo vim /etc/systemd/logind.conf
#HandleLidSwitch=suspend
HandleLidSwitch=ignore
sudo restart systemd-logind
```
[每日Ubuntu小技巧：合上笔记本，系统不睡眠](https://linux.cn/article-2485-1.html)

## 安装ROS

参考官网教程即可[Ubuntu install of ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)

## 安装ZED

首先建立ros工作空间
[Creating a workspace for catkin](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

然后安装zed_cpu，使用cpu转载zed图像
[zed_cpu_ros](https://github.com/willdzeng/zed_cpu_ros)

```
查看zed摄像头工作情况
rosrun image_view image_view image:=/camera/right/image_raw
```

## 安装rosaria

首先安装Aria库，该库通过串口可以获取P3AT机器人的底层数据，包括控制底层运动平台。

```
sudo dpkg -i libaria_2.9.0+ubuntu12+gcc4.6_amd64.deb
cd /usr/local/Aria/examples && ./demo -rp /dev/ttyUSB0
// 修改ttyUSB0权限
sudo usermod -aG dialout $USER
```

然后安装和ROS的接口，使得可以通过ROS对P3AT机器人的底层数据进行获取。参考[How to use ROSARIA](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA)

下一步的工作将rosaria相关的命令做到控制中心主机的界面上。
