void *wstree_new(int length);
void *wstree_new_with_string(char *s);
void wstree_insert(void *obj, int x);
void wstree_erase(void *obj, int x);
int wstree_count(void *obj, int x);
int wstree_no_less_than(void *obj, int x);
int wstree_no_greater_than(void *obj, int x);