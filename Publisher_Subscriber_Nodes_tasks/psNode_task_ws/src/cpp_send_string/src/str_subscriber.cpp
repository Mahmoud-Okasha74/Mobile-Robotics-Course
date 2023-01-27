#include <ros/ros.h>
#include <std_msgs/String.h>

void countCallback(const std_msgs::String::ConstPtr& hello_str)
{
  ROS_INFO("%s", hello_str->data.c_str());
}
int main(int argc, char** argv)
{
  ros::init(argc, argv, "stringSubscriber");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("stringTopic", 1000, countCallback);
  ros::spin();

  return 0;
}