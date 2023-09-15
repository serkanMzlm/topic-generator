#include <iostream>

int main(){

    @[for surname in subscriptions ]@
    std::cout <<" @(surname['topic']) "<< std::endl;
    @[end for]@

    return 0;
}