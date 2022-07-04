# Install Niryo One ROS stack

## Install Required Environment
As shown in https://github.com/NiryoRobotics/niryo_one_ros, the requirements are:
  * Ubuntu 16.04
  * ROS Kinetic (other versions are not supported)

### Install ROS kinetic
The system be be downloaded in [Ubiquity Robotics](https://learn.ubiquityrobotics.com/kinetic_pi_image_downloads). It's a Ubuntu 16.04 desktop with Kinetic pre-installed.

### Install some additional ROS packages

```
sudo apt-get install ros-kinetic-robot-state-publisher ros-kinetic-moveit ros-kinetic-rosbridge-suite ros-kinetic-joy ros-kinetic-ros-control ros-kinetic-ros-controllers ros-kinetic-tf2-web-republisher
```


### Install an additional Python module

The official method is:

```
sudo -H pip install jsonpickle
```

However, you may encount some errors regrading `pip install <package_name>`.

If so, you can use:

```
sudo apt-get update -y
sudo apt-get install -y python-jsonpickle
```

Then, you have successfully downloaded the required package. You can check in the default path:

```
/usr/bin/python2.7/site-package
```
