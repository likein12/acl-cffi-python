void *veci_new();
void veci_push_back(void *obj, int x);
int veci_at(void *obj, int index);
int veci_size(void *obj);
void veci_sub(void *obj, int index, int x);

void *vecll_new();
void vecll_push_back(void *obj, long long x);
long long vecll_at(void *obj, int index);
int vecll_size(void *obj);
void vecll_sub(void *obj, int index, long long val);

void *vecm_new();
void vecm_push_back(void *obj, long long x);
int vecm_at(void *obj, int index);
int vecm_size(void *obj);
void vecm_sub(void *obj, int index, long long x);

int vvi_get(void *obj, int index1, int index2);
int vvi_size(void *obj);
int vvi_size_of_i(void *obj, int index);
