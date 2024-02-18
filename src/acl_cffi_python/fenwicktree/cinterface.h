void *fenwick_tree_ll_new(int n);
void fenwick_tree_ll_add(void *obj, int p, long long x);
long long fenwick_tree_ll_sum(void *obj, int l, int r);
void *fenwick_tree_i_new(int n);
void fenwick_tree_i_add(void *obj, int p, int x);
int fenwick_tree_i_sum(void *obj, int l, int r);