# Install Niryo One ROS stack

## Install Required Environment
The requirements are:
  * Ubuntu 18.04
  * ROS Melodic

The detailed requirement can be found in [Ubuntu 18 Installation](https://docs.niryo.com/dev/ros/v4.1.0/en/source/installation/ubuntu_18.html)

## Install An Additional Python Module

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

## Create A New Workspace

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

## Create SRDF Files
Although there already has a SRDF file in the folder, some mistakes are exsited. Therefore, we need to generate it by ourselves.
1. Launch Moveit Assistant

 ```
 roslaunch moveit_setup_assistant setup_assistant.launch
 ```
 
2. Choose "Create New Moveit Configuration Package".

3. Add `niryo_one_gripper1_n_camera.urdf.xacro` path.
   Now, you can see the preview of your model on the right.
   
   ![Screenshot from 2022-07-11 19-18-37](https://user-images.githubusercontent.com/45569291/178341842-8dc09c43-1394-4f9a-9409-04f538da4490.png)
  
4. In "Self-Collisions" page, you can remain the default setting and click "Generate Collision Matrix".

5. The "Virtual Joints" is ignored.

6. In "Planning Group" page, here we can reference the file in `/catkin_ws_niryo_one/src/niryo_robot_moveit_config/niryo_moveit_config_w_gripper1/config/one/niryo_one.srdf`. It can be derived from the picture that there are two groups, namely "arm" and "tool".

   ![Screenshot from 2022-07-12 10-47-36](https://user-images.githubusercontent.com/45569291/178473466-7191b888-807e-4919-bd32-5ab1eaa19bab.png)
   
   
   Add correspnding joints and links. In `arm group`, we choose **kdl_kinematics_plugin/KDLKinamaticsPlugin** as *Kinematic Solver* and select **RRTConnect** as *Group Default Planner*. In `tool group`, we don't need to set these.
   
   Finally, it looks like this.
   
   ![Screenshot from 2022-07-12 11-09-14](https://user-images.githubusercontent.com/45569291/178476800-7b4cdecb-7d88-4d92-ad56-571de586992f.png)

7. The "Robot Poses" is ignored here.

8. In "End Effectors" page, add as followed:

    ![Screenshot from 2022-07-12 13-51-54](https://user-images.githubusercontent.com/45569291/178506434-e7d69734-7bfc-4666-84d7-38341fce1429.png)

9. In "ROS Controller" page, enter **arm_position_controller** as *Controller Name*. Choose **position_controllers/JointPositionController** as *controller type*.

10. Finally, add author information as you wish. Set generate path as a new folder named `niryo_moveit_config` in your workspace. Click *Generate Package* button.


## Control Robotics Arm in Simulation
1. Back to your workspace and compile configration files.

   ```
   cd ~/niryo_ws
   catkin_make
   ```

2. Open simulation model in Rviz.

   ```
   roslaunch niryo_moveit_config demo.launch
   ```
   
   Some issues may encounter like:
   
   ![Screenshot from 2022-07-12 14-26-45](https://user-images.githubusercontent.com/45569291/178514056-89bba968-0b8f-478e-86c5-d1a324fcc5da.png)
   
   In such situation, just go to `/niryo_moveit_config/config/fake_controllers.yaml` and `/sensors_3d.yaml`. Than delete `initial` and `sensors`. Rerun the command and you will find the error messages have gone.

   ![Screenshot from 2022-07-12 14-33-28](https://user-images.githubusercontent.com/45569291/178515532-caa49972-4b65-44cd-a63c-e89b161c0bab.png)
   
3. Create a new package to store python command files.
   
   ```
   catkin_create_pkg niryo_robot_control roscpp rospy std_msgs
   cd ~/niryo_ws
   catkin_make
   
   mkdir -p niryo_robot_control/scripts
   cd niryo_robot_control/scripts
   touch demo.py
   ```

## Control Physical Robotics Arm

![image](https://user-images.githubusercontent.com/45569291/184678088-9117aad7-85c7-4362-a00a-1c8c7005aabd.png)
