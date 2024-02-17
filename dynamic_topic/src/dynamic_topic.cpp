#include "dynamic_topic.hpp"

using namespace std::placeholders;

DynamicTopic::DynamicTopic(): Node("dynamic_topic_node"){
    pub.twist = this->create_publisher<twistMsg>("/out/twist", 10);

    sub.float32 = this->create_subscription<float32Msg>("/in/float32", 10,
                std::bind(&DynamicTopic::subFloat32Callback,this,_1)); 
    sub.laser_scan = this->create_subscription<laser_scanMsg>("/in/lidar", 10,
                std::bind(&DynamicTopic::subLaserScanCallback,this,_1)); 

    timer.twist = this->create_wall_timer(std::chrono::milliseconds(P2F(5)),
                        std::bind(&DynamicTopic::pubTwistCallback, this));

    RCLCPP_INFO(this->get_logger(), "Topic Started.");
}

DynamicTopic::~DynamicTopic(){

}

void DynamicTopic::pubTwistCallback(){
    twistMsg msg;
    pub.twist->publish(msg);
}

void DynamicTopic::subFloat32Callback(const float32Msg msg){
    (void)msg;
}
void DynamicTopic::subLaserScanCallback(const laser_scanMsg msg){
    (void)msg;
}
