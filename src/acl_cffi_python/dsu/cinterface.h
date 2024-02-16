void *dsu_new(int n);
int dsu_merge(void *obj, int a, int b);
int dsu_same(void *obj, int a, int b);
int dsu_leader(void *obj, int a);
int dsu_size(void *obj, int a);