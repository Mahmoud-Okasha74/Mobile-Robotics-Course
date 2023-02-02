#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker():
    rospy.init_node("countPublisher_node")
    pub = rospy.Publisher("countTopic",Int32,queue_size=1)
    rate = rospy.Rate(2)
    count=100
    while not rospy.is_shutdown():
        rospy.loginfo(count)
        pub.publish(count)
        rate.sleep()
        count += 1





if __name__=='__main__' :
    try:
        talker()
    except rospy.ROSInterruptException :
        pass
    
