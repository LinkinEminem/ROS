#!/usr/bin/env python

import rospy
import tf
from niryo_robot_control.srv import *


def send_position():
    rospy.init_node("send_position")
    rospy.wait_for_service('/pick_litter')
    try:
        send = rospy.ServiceProxy('/pick_litter', Litter)
        response = send(0.1, 0.1, 0.1, "plastic")
        return response.rst
    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_position()
