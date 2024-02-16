void *segtree_rmq_max_new(int n);
void *segtree_rmq_max_new_with_vec(void *obj);
void segtree_rmq_max_set(void *obj, int p, long long x);
long long segtree_rmq_max_get(void *obj, int p);
long long segtree_rmq_max_prod(void *obj, int l, int r);
int segtree_rmq_max_max_right(void *obj, int l, int threshold);
int segtree_rmq_max_min_left(void *obj, int r, int threshold);