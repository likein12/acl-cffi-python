#ifndef CFFI_GRIDMAP_HPP
#define CFFI_GRIDMAP_HPP 1
#include "../static/cppinterface.hpp"

struct gridmap {
    static_string mp;
    int h,w;
    gridmap(int _h, int _w) : h(_h), w(_w), mp(static_string(h*w+1)){
    }
    void update(char* input){
        for(int i=0;i<h;++i) for(int j=0;j<w;++j) mp.push_back(input[i*w+j]);
    }
};

#endif