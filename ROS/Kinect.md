
## Kinect with ROS-Kinectic 

~~~
sudo apt-get install libfreenect-dev

sudo apt-get install ros-kinetic-freenect-launch
sudo apt-get install ros-kinetic-depthimage-to-laserscan

roscore
roslaunch freenect_launch freenect.launch
~~~

use rviz config from https://gist.github.com/WinKILLER/df1a37f0406e5370abf39534bd8bbde1 (tried with kinect_view.rviz)