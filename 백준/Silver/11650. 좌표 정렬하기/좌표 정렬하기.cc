#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);
    
    int N, x, y;
    cin >> N;

    vector<pair<int, int>> v;

    for (int i = 0; i < N; i++) {
        cin >> x >> y;  // N개의 좌표 받기
        v.push_back(make_pair(x, y));   // pair 만들어 벡터에 넣기
    }

    sort(v.begin(), v.end());   // x, y 순서대로 오름차순 정렬

    for (int i = 0; i < N; i++)
        cout << v[i].first << " " << v[i].second << "\n";

    return 0;
}