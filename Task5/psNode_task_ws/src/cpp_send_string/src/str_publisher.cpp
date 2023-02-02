#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "stringPublisher");
  ros::NodeHandle nh;
  ros::Rate loop_rate(2);
  ros::Publisher pub = nh.advertise<std_msgs::String>("stringTopic", 1000);
  std_msgs::String hello_str;
  std::stringstream ss;
  ss << "I am Learning Robotics and ROS";
  hello_str.data = ss.str();
  while (ros::ok())
  {
    ROS_INFO("%s", hello_str.data.c_str());
    pub.publish(hello_str);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
