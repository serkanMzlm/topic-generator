#ifndef __DYNAMIC_TOPIC__
#define __DYNAMIC_TOPIC__

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "geometry_msgs/msg/twist.hpp"

#define P2F(X) (1/X)

using float32Msg = std_msgs::msg::Float32; 
using laser_scanMsg = sensor_msgs::msg::LaserScan; 
using twistMsg = geometry_msgs::msg::Twist; 

typedef struct{
        rclcpp::Publisher<twistMsg>::SharedPtr twist;
    
}Pub_t;

typedef struct{
        rclcpp::Subscription<float32Msg>::SharedPtr float32;
        rclcpp::Subscription<laser_scanMsg>::SharedPtr laser_scan;
    
}Sub_t;

typedef struct{
        rclcpp::TimerBase::SharedPtr twist;
        
}Time_t;

class DynamicTopic: public rclcpp::Node{
private:
    Pub_t pub;
    Sub_t sub;
    Time_t timer;

public:
    DynamicTopic();
    ~DynamicTopic();

    void pubTwistCallback();

    void subFloat32Callback(const float32Msg);
    void subLaserScanCallback(const laser_scanMsg);

};

#endif