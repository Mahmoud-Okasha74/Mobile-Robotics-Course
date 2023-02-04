#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def publisher():
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=True)
    rospy.init_node("move_turtle_node",anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        mov=Twist()
        mov.linear.x=0.5
        pub.publish(mov)
        rate.sleep()

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass