#include<bits/stdc++.h>
using namespace std;

void bfsTraversal(int V, vector<int> adjList[]){

    vector<int> visited(V+1);
    
    vector<int> bfs;
    queue<int> q;

    start = 1;

    q.push(start);

    while(!q.empty()){
        int top = q.front();
        q.pop();
        bfs.push_back(top);
        for(int i:adjList[top]){
            if(!visited[i]){
                visited[i] = 1;
                q.push(i);
            }
        }
    }

}
