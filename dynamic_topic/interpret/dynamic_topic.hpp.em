#ifndef __DYNAMIC_TOPIC__
#define __DYNAMIC_TOPIC__

#include "rclcpp/rclcpp.hpp"
@[for inc in includes.keys()]@
#include "@(inc).hpp"
@[end for]@

#define P2F(X) (1/X)

@[for key, value in includes.items()]@
using @(value[0])Msg = @(value[1]['type']); 
@[end for]@

typedef struct{
    rclcpp::Publisher<rangeMsg>::SharedPtr range;
}Pub_t;

typedef struct{
    @[for key, value in includes.items()]@
    rclcpp::Subscription<@(value[0])Msg>::SharedPtr @(value[0]);
    @[end for]@
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