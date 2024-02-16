void *two_sat_new(int n);
void two_sat_add_clause(void *obj, int i, int f, int j, int g);
int two_sat_satisfiable(void *obj);
void *two_sat_answer(void *obj);