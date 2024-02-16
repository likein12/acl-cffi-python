typedef struct {
    // modify
    // cppinterface.hppの定義と揃える
} segtree_TAG_S;

// modify
segtree_TAG_S segtree_TAG_S_new(long long a, int b);

void *vec_segtree_TAG_S_new();
void *vec_segtree_TAG_S_new_with_size(int n);
void vec_segtree_TAG_S_push_back(void *obj, segtree_TAG_S &x);
segtree_TAG_S vec_segtree_TAG_S_at(void *obj, int index);
int vec_segtree_TAG_S_size(void *obj);
void vec_segtree_TAG_S_sub(void *obj, int index, segtree_TAG_S &x);

void *segtree_TAG_new(int n);
void *segtree_TAG_new_with_vec(void *obj);
void segtree_TAG_set(void *obj, int p, segtree_TAG_S x);
segtree_TAG_S segtree_TAG_get(void *obj, int p);
segtree_TAG_S segtree_TAG_prod(void *obj, int l, int r);
int segtree_TAG_max_right(void *obj, int l, int threshold);
int segtree_TAG_min_left(void *obj, int r, int threshold);