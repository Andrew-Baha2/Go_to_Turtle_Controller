#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt

prev_x =0
prev_y =0
prev_theta=0


def pose_callback(pose):
    global prev_x
    global prev_y
    global prev_theta

    prev_x= pose.x
    prev_y=pose.y
    prev_theta=pose.theta

def go_to_controller(xgoal,ygoal):
    global prev_x
    global prev_y
    global prev_theta

    cmd=Twist()
    while(True):
        kv=rospy.get_param("beta",2)
        kw=rospy.get_param("phai",10)
        distance=abs(math.sqrt(((xgoal-prev_x) ** 2 )+((ygoal-prev_y) ** 2)))
        linear_v=float(kv*distance)
        angular_v=kw*(-1*(prev_theta)+math.atan2((ygoal-prev_y),(xgoal-prev_x)))
        cmd.linear.x=linear_v
        cmd.angular.z=angular_v 
        pub.publish(cmd)
        if distance<=0.01:
            cmd.linear.x=0
            cmd.angular.z=0
            rospy.loginfo("Goal achieved")
            break


if __name__ == '__main__':
    try:
        rospy.init_node("turtle_controller")
        while (True):
            pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
            sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
            rospy.loginfo("Node started")
            rospy.loginfo("Enter Goal Coordinates")
            x_coordinate=input("x : ")
            y_coordinate=input("y : ")
            go_to_controller(float(x_coordinate),float(y_coordinate))
        rospy.spin()
    except rospy.ROSInterruptException:
        pass