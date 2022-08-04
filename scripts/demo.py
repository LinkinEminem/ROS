#!/usr/bin/env python2

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


def main():
    rospy.init_node("niryo_move")  # Initialize rospy node
    robot = moveit_commander.RobotCommander()  # Instantiate a RobotCommander object
    scene = moveit_commander.PlanningSceneInterface()  # Instantiate a PlanningSceneInterface object. 
    group_name = "niryo_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher(
    "/move_group/display_planned_path",
    moveit_msgs.msg.DisplayTrajectory,
    queue_size=20,
    )


    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = 0.2
    pose_goal.position.y = 0.0
    pose_goal.position.z = 0.1

    move_group.set_pose_target(pose_goal)
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()


if __name__ == "__main__":
    main()