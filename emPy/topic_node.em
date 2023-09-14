#include <iostream>

int main(){

    @[for surname in pub]@
    std::cout << @(surname) << std::endl;
    @[end for]@
    return 0;
}