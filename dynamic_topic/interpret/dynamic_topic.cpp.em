#include "dynamic_topic.hpp"

using namespace std::placeholders;

DynamicTopic::DynamicTopic(): Node("dynamic_topic_node"){
@[for key, value in publications.items()]@
    pub.@(key) = this->create_publisher<@(key)Msg>("@(value['topic'])", 10);
@[end for]@

@[for key, value in subscriptions.items()]@
    sub.@(key) = this->create_subscription<@(key)Msg>("@(value['topic'])", 10,
                std::bind(&DynamicTopic::sub@(value['type'].split('::')[-1])Callback,this,_1)); 
@[end for]@

@[for key, value in publications.items()]@
    timer.@(key) = this->create_wall_timer(std::chrono::milliseconds(P2F(@(value['hz']))),
                        std::bind(&DynamicTopic::pub@(value['type'].split('::')[-1])Callback, this));
@[end for]@

    RCLCPP_INFO(this->get_logger(), "Topic Started.");
}

DynamicTopic::~DynamicTopic(){

}

@[for key, value in publications.items()]@
void DynamicTopic::pub@(value['type'].split('::')[-1])Callback(){
    @(key)Msg msg;
    pub.@(key)->publish(msg);
}
@[end for]@

@[for key, value in subscriptions.items()]@
void DynamicTopic::sub@(value['type'].split('::')[-1])Callback(const @(key)Msg msg){
    (void)msg;
}
@[end for]@