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

typedef unsigned int uint;

static_arri static_arri_new(int sz);
static_arri static_arri_new_with_value(int n, int x, int sz);
static_arrll static_arrll_new(int sz);
static_arrll static_arrll_new_with_value(int n, int x, int sz);

uint mint_normalize(long long a);
uint mint_add(uint a, long long b);
uint mint_substract(uint a, long long b);
uint mint_prod(uint a, long long b);
uint mint_div(uint a, long long b);
uint mint_pow(uint a, long long b);
uint mint_radd(long long a, uint b);
uint mint_rsubstract(long long a, uint b);
uint mint_rprod(long long a, uint b);
uint mint_rdiv(long long a, uint b);
