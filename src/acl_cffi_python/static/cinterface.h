typedef struct  {
    int *ptr;
    int _max_len;
    int _now_len;
} static_arri;

typedef struct  {
    long long *ptr;
    int _max_len;
    int _now_len;
} static_arrll;

typedef struct  {
    unsigned int *ptr;
    int _max_len;
    int _now_len;
} static_arrui;

typedef struct  {
    char *ptr;
    int _max_len;
    int _now_len;
} static_string;

typedef unsigned int uint;

static_arri static_arri_new(int max_len);
static_arri static_arri_new_with_value(int n, int x, int max_len);
static_arrll static_arrll_new(int max_len);
static_arrll static_arrll_new_with_value(int n, long long x, int max_len);
static_arrui static_arrui_new(int max_len);
static_arrui static_arrui_new_with_value(int n, unsigned int x, int max_len);
static_arrui static_arrui_new_with_novalue(int n, int max_len);
static_string static_string_new(int max_len);
static_string static_string_new_with_value(int n, char x, int max_len);
