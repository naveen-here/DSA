void set3Cond(int i, int j,  int x){
    const int x2=1<<x;
	Row[i]|=x2;
    Col[j]|=x2;
    const int bidx=(i/3)*3 +j/3;
    Block[bidx]|=x2;
}