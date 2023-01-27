#include<ros/ros.h>
#include<std_msgs/Int32.h>

int main (int argc,char**argv)
{
    ros::init(argc,argv,"countPublisher");
    ros::NodeHandle nh;
    ros::Rate loop_rate(2);
    ros::Publisher pub = nh.advertise<std_msgs::Int32>("countTopic",1000);
    std_msgs::Int32 count;
    count.data = 100;
    while (ros::ok())
    {
        ROS_INFO("%d",count);
        pub.publish(count);
        ros::spinOnce();
        loop_rate.sleep();
        ++count.data;  
    }
    
    return 0;
}
