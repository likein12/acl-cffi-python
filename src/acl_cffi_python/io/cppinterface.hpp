#ifndef CFFI_IO_HPP
#define CFFI_IO_HPP 1
#include <cstdio>
#include <cstdlib>
#include "../std/vector/cppinterface.hpp"

extern "C" {
    static long long scanner_ll() {
        long long x = 0, f = 1, c;
        while (c = getchar_unlocked(), c < 48 || c > 57) if (c == 45) f = -f;
        while (47 < c && c < 58) {
            x = x * 10 + c - 48;
            c = getchar_unlocked();
        }
        return f * x;
    }

    static void* scanner_vecll(int n) {
        vecll *ret = new vecll(n);
        for (int i=0;i<n;++i) ret->at(i) = scanner_ll();
        return ret;
    }

    static void* scanner_vecm(int n) {
        vecm *ret = new vecm(n);
        for (int i=0;i<n;++i) ret->at(i) = scanner_ll();
        return ret;
    }

    static char* scanner_string(int n) {
        char* res = (char*)malloc((n+1)*sizeof(char));
        char c = getchar_unlocked();
        while (c < 32) c = getchar_unlocked();
        int i = 0;
        while (c >= 32) {
            res[i] = c;
            c = getchar_unlocked();
            i++;
        }
        res[i] = '\0';
        return res;
    }

    static void printer_ll(long long x) {
        if (x < 0) {
            putchar_unlocked('-');
            x = -x;
        }
        if (x >= 10) {
            printer_ll(x / 10);
        }
        putchar_unlocked(x - x / 10 * 10 + 48);
    }
    
    static void printer_ll_one(long long x) {
        printer_ll(x);
        putchar_unlocked('\n');
    }

    static void printer_array_v_ll(void* x) {
        int n = ((vecll*)x)->size();
        for (int i=0;i<n-1;++i) {
            printer_ll(((vecll*)x)->at(i));
            putchar_unlocked(' ');
        }
        printer_ll(((vecll*)x)->at(n-1));
        putchar_unlocked('\n');
    }
    
    static void printer_array_h_ll(void* x) {
        int n = ((vecll*)x)->size();
        for (int i=0;i<n;++i) {
            printer_ll(((vecll*)x)->at(i));
            putchar_unlocked('\n');
        }
    }

    static void printer_array_v_m(void* x) {
        int n = ((vecm*)x)->size();
        for (int i=0;i<n-1;++i) {
            printer_ll(((vecm*)x)->at(i).val());
            putchar_unlocked(' ');
        }
        printer_ll(((vecm*)x)->at(n-1).val());
        putchar_unlocked('\n');
    }
    
    static void printer_array_h_m(void* x) {
        int n = ((vecm*)x)->size();
        for (int i=0;i<n;++i) {
            printer_ll(((vecm*)x)->at(i).val());
            putchar_unlocked('\n');
        }
    }

}

#endif