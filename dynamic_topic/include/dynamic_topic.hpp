#ifndef __DYNAMIC_TOPIC__
#define __DYNAMIC_TOPIC__

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/range.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "std_msgs/msg/float32.hpp"
#include "sensor_msgs/msg/imu.hpp"

#define P2F(X) (1/X)

using rangeMsg = sensor_msgs::msg::Range; 
using twistMsg = geometry_msgs::msg::Twist; 
using float32Msg = std_msgs::msg::Float32; 
using imuMsg = sensor_msgs::msg::Imu; 

typedef struct{
        rclcpp::Publisher<imuMsg>::SharedPtr imu;
        rclcpp::Publisher<rangeMsg>::SharedPtr range;
    
}Pub_t;

typedef struct{
        rclcpp::Subscription<rangeMsg>::SharedPtr range;
        rclcpp::Subscription<twistMsg>::SharedPtr twist;
        rclcpp::Subscription<float32Msg>::SharedPtr float32;
    
}Sub_t;

typedef struct{
        rclcpp::TimerBase::SharedPtr imu;
        rclcpp::TimerBase::SharedPtr range;
        
}Time_t;

class DynamicTopic: public rclcpp::Node{
private:
    Pub_t pub;
    Sub_t sub;
    Time_t timer;

public:
    DynamicTopic();
    ~DynamicTopic();

    void pubImuCallback();
    void pubRangeCallback();

    void subRangeCallback(const rangeMsg);
    void subTwistCallback(const twistMsg);
    void subFloat32Callback(const float32Msg);

};

#endif