#ifndef __DYNAMIC_TOPIC__
#define __DYNAMIC_TOPIC__

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "sensor_msgs/msg/imu.hpp"
#include "sensor_msgs/msg/range.hpp"
#include "std_msgs/msg/float32.hpp"
#define P2F(X) (1/X)






typedef struct{
    rclcpp::Publisher<rangeMsg>::SharedPtr range;
}Pub_t;

typedef struct{
    rclcpp::Subscription<rangeMsg>::SharedPtr range;
}Sub_t;

typedef struct{
    rclcpp::TimerBase::SharedPtr range;
}Time_t;

class DynamicTopic: public rclcpp::Node{
public:
    DynamicTopic();
    void pubRangeCallback();
    void subRangeCallback(const rangeMsg);

private:
    Pub_t pub;
    Sub_t sub;
    Time_t timer;
};

#endif