#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

def publisher():
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=True)
    rospy.init_node("move_turtle_node",anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        mov=Twist()
        print ("please input a linear (x) velocity in the range [2,6] (floating point allowed) \n")
        mov.linear.x = float(input("x : "))
        print ("please input an angular (z) velocity [1,3] (floating point allowed)")
        mov.angular.z = float(input("z : "))
        pub.publish(mov)
        rate.sleep()

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass