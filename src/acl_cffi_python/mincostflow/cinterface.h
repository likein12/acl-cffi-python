void *mcf_graph_ll_ll_new(int n);
int mcf_graph_ll_ll_add_edge(void *obj, int from, int to, long long cap, long long cost);
pll mcf_graph_ll_ll_flow(void *obj, int s, int t);
pll mcf_graph_ll_ll_flow_with_limit(void *obj, int s, int t, long long flow_limit);

// int mcf_graph_ll_ll_edge_from(void *obj);
// int mcf_graph_ll_ll_edge_to(void *obj);
// int mcf_graph_ll_ll_edge_cap(void *obj);
// int mcf_graph_ll_ll_edge_flow(void *obj);
// int mcf_graph_ll_ll_edge_cost(void *obj);

typedef struct 
{
    int frm, to;
    long long cap, flow, cost;
} mcf_graph_ll_ll_edge;

mcf_graph_ll_ll_edge mcf_graph_ll_ll_get_edge(void *obj, int i);
// edges()は作らなくてよいと判断, Python側でiterationを回して取得してもそこまでロスじゃないはず
