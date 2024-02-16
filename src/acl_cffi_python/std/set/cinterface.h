void *setll_new();
void setll_insert(void *obj, long long x);
void *setll_find(void *obj, long long x);
void setll_erase(void *obj, void *itr);
void setll_erase_val(void *obj, long long x);
void setll_clear(void *obj);
int setll_contain(void *obj, long long x);
int setll_size(void *obj);
void *setll_begin(void *obj);
void *setll_end(void *obj);
void *setll_rbegin(void *obj);
void *setll_rend(void *obj);
int setll_itr_compare(void *itr1, void *itr2);
int setll_ritr_compare(void *ritr1, void *ritr2);

void *setll_lower_bound(void *obj, long long x);
void *setll_upper_bound(void *obj, long long x);

long long setll_itr_deref(void *obj);
void setll_itr_increment(void *obj);
void setll_itr_decrement(void *obj);
long long setll_ritr_deref(void *obj);
void setll_ritr_increment(void *obj);
void setll_ritr_decrement(void *obj);

void *mlsetll_new();
void mlsetll_insert(void *obj, long long x);
void *mlsetll_find(void *obj, long long x);
void mlsetll_erase(void *obj, void *itr);
void mlsetll_erase_val_one(void *obj, long long x);
void mlsetll_erase_val_all(void *obj, long long x);
void mlsetll_clear(void *obj);
int mlsetll_contain(void *obj, long long x);
int mlsetll_size(void *obj);
void *mlsetll_begin(void *obj);
void *mlsetll_end(void *obj);
void *mlsetll_rbegin(void *obj);
void *mlsetll_rend(void *obj);
int mlsetll_itr_compare(void *itr1, void *itr2);
int mlsetll_ritr_compare(void *ritr1, void *ritr2);

void *mlsetll_lower_bound(void *obj, long long x);
void *mlsetll_upper_bound(void *obj, long long x);

long long mlsetll_itr_deref(void *obj);
void mlsetll_itr_increment(void *obj);
void mlsetll_itr_decrement(void *obj);
long long mlsetll_ritr_deref(void *obj);
void mlsetll_ritr_increment(void *obj);
void mlsetll_ritr_decrement(void *obj);

int mlsetll_count(void *obj, long long x);