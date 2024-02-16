void *pll_new(long long f, long long s);
long long pll_first(void *obj);
long long pll_second(void *obj);
void pll_set_first(void *obj, long long x);
void pll_set_second(void *obj, long long x);

// for dijkstra
void *plli_new(long long f, int s);
long long plli_first(void *obj);
int plli_second(void *obj);
void plli_set_first(void *obj, long long x);
void plli_set_second(void *obj, int x);

void *pmint_new(long long f, long long s);
int pmint_first(void *obj);
int pmint_second(void *obj);
void pmint_set_first(void *obj, long long x);
void pmint_set_second(void *obj, long long x);
