# Install Niryo One ROS stack

## Install Required Environment
The requirements are:
  * Ubuntu 18.04
  * ROS Melodic

The detailed requirement can be found in [Ubuntu 18 Installation](https://docs.niryo.com/dev/ros/v4.1.0/en/source/installation/ubuntu_18.html)

## Install an additional Python module

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

## Clone GitHub Resource


```
git clone https://github.com/NiryoRobotics/ned_ros
```

# Build URDF (Unified Robot Description Format)

## Create a new workspace

+ Create a new folder `niryo_ws` and initialize worksapce.

 ```
 mkdir -p niryo_ws/src
 cd niryo/src
 catkin_init_workspace
 ```

+ Copy `niryo_robot_description` into new folder.
  Then, compile the folder.

 ```
 catkin_make
 ```

Don't forget to add new `setup.bash` command into `~/.bashrc`.

## Create SRDF files
1. Launch Moveit Assistant

 ```
 roslaunch moveit_setup_assistant setup_assistant.launch
 ```
 
2. Choose "Create New Moveit Configuration Package".
3. Add `niryo_one_gripper1_n_camera.urdf.xacro` path.
   Now, you can see the preview of your model on the right.
   
  ![Screenshot from 2022-07-11 19-18-37](https://user-images.githubusercontent.com/45569291/178341842-8dc09c43-1394-4f9a-9409-04f538da4490.png)
  
4. In "Self-Collisions" page, you can remain the default setting and click "Generate Collision Matrix"
5. The "Virtual Joints" is ignored here.
6. In "Planning Group" page, 
