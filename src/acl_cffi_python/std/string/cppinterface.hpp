#ifndef CFFI_STD_STRING_HPP
#define CFFI_STD_STRING_HPP 1
#include <string>

extern "C" {
    using string = std::string;
    void *string_new(char *s){ return new string(s);}
    void string_push_back(void *obj, int x) { ((string*)obj)->push_back(x);}    
    char string_at(void *obj, int index) { return ((string*)obj)->at(index);}
    int string_size(void *obj) { return ((string*)obj)->size();}
    void string_sub(void *obj, int index, char x) {(*((string*)obj))[index] = x;}
}

#endif

