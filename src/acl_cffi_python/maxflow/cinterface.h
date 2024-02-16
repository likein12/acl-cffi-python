void *mf_graph_ll_new(int n);
int mf_graph_ll_add_edge(void *obj, int from, int to, long long cap);
long long mf_graph_ll_flow(void *obj, int s, int t);
long long mf_graph_ll_flow_with_limit(void *obj, int s, int t, long long flow_limit);

int mf_graph_ll_edge_from(void *obj);
int mf_graph_ll_edge_to(void *obj);
long long mf_graph_ll_edge_cap(void *obj);
long long mf_graph_ll_edge_flow(void *obj);

void *mf_graph_ll_get_edge(void *obj, int i);
// edges()は作らなくてよいと判断, Python側でiterationを回して取得してもそこまでロスじゃないはず
void mf_graph_ll_change_edge(void *obj, int i, long long new_cap, long long new_flow);
