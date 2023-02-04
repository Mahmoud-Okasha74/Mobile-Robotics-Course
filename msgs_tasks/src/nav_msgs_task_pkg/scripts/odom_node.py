#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry


def subscribe ():
    rospy.init_node ("odom_subscribe_node")
    rospy.Subscriber("/odom_topic",Odometry,callback)
    rospy.spin()

def callback (data):
    rospy.loginfo("The odometry data :")
    #rospy.loginfo(data)
    


if __name__=='__main__':
    subscribe()