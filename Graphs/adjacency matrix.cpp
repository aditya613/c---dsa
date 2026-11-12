
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;

    //n*n matrix 
    vector<vector<int>> adjMatrix(n, vector<int>(n, 0));

    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;

        //for undirected graph
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;


        //in case of directed graph
        adjMatrix[u][v] = 1;

    }
}