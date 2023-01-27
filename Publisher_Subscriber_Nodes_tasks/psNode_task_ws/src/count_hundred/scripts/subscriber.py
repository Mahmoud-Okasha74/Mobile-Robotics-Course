#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def listner():
    rospy.init_node("countSubscriber_node")
    rospy.Subscriber("countTopic",Int32,callback)
    rospy.spin()

def callback(msgdata):
    rospy.loginfo(msgdata.data)    




if __name__=='__main__':
    listner()