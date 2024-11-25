#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, M, V;    // 정점개수, 간선개수, 시작정점
vector<vector<int>> adj;  // 인접 리스트
bool v1[1000], v2[1000];  // visited

void dfs(int s) {
    v1[s] = true;
    cout << s << " ";
    for (int i = 0; i < adj[s].size(); i++)
    {
        if (v1[adj[s][i]]) continue;
        dfs(adj[s][i]);
    }
}

void bfs(int s) {
    v2[s] = true;
    queue<int> q;
    q.push(s);
    int c;
    while (!q.empty()) {
        c = q.front();  // 맨 앞 값 접근
        q.pop();        // 맨 앞 값 삭제
        cout << c << " ";
        for (int i = 0; i < adj[c].size(); i++) {
            if (v2[adj[c][i]]) continue;
            v2[adj[c][i]] = true;
            q.push(adj[c][i]);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> V;
    adj.resize(N+1);  // 인접리스트 크기 동적 할당

    int a, b;
    while (cin >> a >> b) { // 간선 추가
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    // 인접리스트 오름차순 정렬
    for (int i = 1; i <= N; i++) {  // 1부터 N까지
        sort(adj[i].begin(), adj[i].end());
    }

    dfs(V);
    cout << "\n";
    bfs(V);
    return 0;
}