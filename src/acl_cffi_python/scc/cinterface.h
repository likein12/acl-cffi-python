void *scc_graph_new(int n);
void scc_graph_add_edge(void *obj, int from, int to);
void *scc_graph_scc(void *obj);