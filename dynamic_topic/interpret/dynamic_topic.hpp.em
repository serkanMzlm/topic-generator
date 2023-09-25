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
    @[for key, value in publications.items()]@
    rclcpp::Publisher<@(key)Msg>::SharedPtr @(key);
    @[end for]@

}Pub_t;

typedef struct{
    @[for key, value in subscriptions.items()]@
    rclcpp::Subscription<@(key)Msg>::SharedPtr @(key);
    @[end for]@

}Sub_t;

typedef struct{
    @[for key, value in publications.items()]@
    rclcpp::TimerBase::SharedPtr @(key);
    @[end for]@
    
}Time_t;

class DynamicTopic: public rclcpp::Node{
private:
    Pub_t pub;
    Sub_t sub;
    Time_t timer;

public:
    DynamicTopic();
    ~DynamicTopic();

@[for key, value in publications.items()]@
    void pub@(value['type'].split('::')[-1])Callback();
@[end for]@

@[for key, value in subscriptions.items()]@
    void sub@(value['type'].split('::')[-1])Callback(const @(key)Msg);
@[end for]@

};

#endif