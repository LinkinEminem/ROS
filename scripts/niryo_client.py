#!/usr/bin/env python

import rospy
from niryo_robot_control.srv import *


def callback_arm(msg):
        try:
                rospy.wait_for_service('/niryo_move_arm')
                niryo_client = rospy.ServiceProxy('/niryo_move_arm', ArmControl)
                response = niryo_client(msg)
                rospy.loginfo(response.rst)
                return ArmControlResponse(response.rst)
        except (rospy.ServiceException):
                pass


def callback_joint(msg):
        try:
                print(msg)
                rospy.wait_for_service('/niryo_move_joint')
                niryo_client = rospy.ServiceProxy('/niryo_move_joint', JointControl)
                response = niryo_client(msg)
                rospy.loginfo(response.rst)
                return JointControlResponse(response.rst)
        except (rospy.ServiceException):
                pass        


def callback_gripper(msg):
        try:
                print(msg)
                rospy.wait_for_service('/niryo_move_gripper')
                niryo_client = rospy.ServiceProxy('/niryo_move_gripper', GripperControl)
                response = niryo_client(msg)
                rospy.loginfo(response.rst)
                return GripperControlResponse(response.rst)
        except Exception as e:
                print(e)           


def niryo_client():
        rospy.init_node('niryo_client')
        rospy.Service('/niryo_arm_control_gui', ArmControl, callback_arm)
        rospy.Service('/niryo_joint_control_gui', JointControl, callback_joint)
        rospy.Service('/niryo_gripper_control_gui', GripperControl, callback_gripper)
        rospy.spin()


if __name__ == "__main__":
        niryo_client()

