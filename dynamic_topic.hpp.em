#include <iostream>

int main(){

    @[for surname in type_includes]@
    std::cout <<" @(surname) "<< std::endl;
    @[end for]@
    return 0;
}