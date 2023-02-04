#! /usr/bin/env python3
import rospy
from robot_age_pkg.msg import age
def publisher ():
    pub = rospy.Publisher("robot_age_topic",age,queue_size=1)
    rospy.init_node("robot_age_publisher_node",anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        robot_age = age()
        robot_age.years=2
        robot_age.months=5
        robot_age.days=7
        pub.publish(robot_age)
        rate.sleep()

if __name__=='__main__':
    try :
        publisher ()
    except rospy.ROSInternalException :
        pass
