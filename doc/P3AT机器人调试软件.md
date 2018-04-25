# P3AT机器人调试软件

该软件具备以下功能：
- 显示ZED双目摄像头采集图像
- 控制P3AT机器人运动（前后左右、停止）
- 显示P3AT机器人位置、电池信息
- 显示P3AT机器人声纳传感器信息
- 显示P3AT机器人碰撞环信息

## 界面设计

参考界面

![](http://chenguanfuqq.gitee.io/tuquan2/img_2018_4/stereo_robot_view.jpeg)

![](http://chenguanfuqq.gitee.io/tuquan2/img_2018_4/robot_view_1.png)

![](http://www.pyqtgraph.org/images/plotting.png)数据显示界面优美

![](http://www.pyqtgraph.org/images/pyqtgraph-3d.png)3D绘图

## 注意点

由于调试软件都通过ROS多机架构进行通讯，同时调试软件使用python编写，其中发现一个问题，
python程序无法直接对多机系统的话题进行发布，该话题只能主机实现订阅。这里提供一个解决思路，使用
python程序发布一个话题，同时本地用cpp编写一个节点监听这个话题，如果监听到则转发给机器人。但是
python监听多机的话题不存在问题。

基于上述解决方案，编写了一个freespace_multi_msg的程序

```
rosrun freespace_multi_msg freespace_multi_msg
```

[Subscribing and publishing geometry/Twist messages from Turtlesim](https://answers.ros.org/question/259708/subscribing-and-publishing-geometrytwist-messages-from-turtlesim/)

[Writing a Simple Publisher and Subscriber (C++)](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)

## 监听发布

根据以上解决了机器人发布监听信息的问题，基于这些信息的格式显示在主界面上，目前先完成电量显示，运动控制。
声呐传感器信息和碰撞环信息由于采用的消息格式来自于rosaria，而rosaria不能直接在pycharm中加载，因此暂时不加入。


[How to use ROSARIA](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA)

[ROSARIA](http://wiki.ros.org/ROSARIA)


