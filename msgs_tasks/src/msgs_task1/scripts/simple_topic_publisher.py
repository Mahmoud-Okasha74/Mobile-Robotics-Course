#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node("topicPublisher")
pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size =10)
rate = rospy.Rate(1)
var = Twist()
var.linear.x = 0.5
var.angular.z = 0.5
while not rospy.is_shutdown() :
    pub.publish(var)
    rate.sleep()
