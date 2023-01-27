#include<ros/ros.h>
#include<std_msgs/Int32.h>

void countCallback (const std_msgs::Int32::ConstPtr &msg)
{
    ROS_INFO("%d",msg->data);
}
int main (int argc,char**argv)
{
    ros::init(argc,argv,"countSubscriber");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("countTopic",1000,countCallback);
    ros::spin();

    return 0;    
}