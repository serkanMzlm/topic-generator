#include "dynamic_topic.hpp"


int main(int argc, char ** args){
  rclcpp::init(argc, args);
  rclcpp::spin(std::make_shared<DynamicTopic>());
  rclcpp::shutdown();
  return 0;
}