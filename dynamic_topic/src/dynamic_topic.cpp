#include "dynamic_topic.hpp"

using namespace std::placeholders;

DynamicTopic::DynamicTopic(): Node("dynamic_topic_node"){
    sub.range = this->create_subscription<rangeMsg>("/in/range", 10,
                std::bind(&DynamicTopic::subRangeCallback, this, _1));
    pub.range = this->create_publisher<rangeMsg>("/out/range", 10);
    timer.range   = this->create_wall_timer(std::chrono::milliseconds(P2F(20)),
                    std::bind(&DynamicTopic::pubRangeCallback, this));
    RCLCPP_INFO(this->get_logger(), "Topic Started.");

}

void DynamicTopic::pubRangeCallback(){

}

void DynamicTopic::subRangeCallback(const rangeMsg msg){

}

int main(int argc, char ** args){
  rclcpp::init(argc, args);
  rclcpp::spin(std::make_shared<DynamicTopic>());
  rclcpp::shutdown();
  return 0;
}