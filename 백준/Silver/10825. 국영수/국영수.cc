#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Stu {
    string name;
    int k, e, m;
};

bool compare(const Stu& a, const Stu& b) {
    if (a.k != b.k) return a.k > b.k;
    if (a.e != b.e) return a.e < b.e;
    if (a.m != b.m) return a.m > b.m;
    return a.name < b.name;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;
    
    vector<Stu> students;
    for (int i = 0; i < N; i++) {
        Stu tmp;    // 임시 구조체
        cin >> tmp.name >> tmp.k >> tmp.e >> tmp.m;
        students.push_back(tmp);
    }

    // 조건에 맞게 정렬
    sort(students.begin(), students.end(), compare);

    for (const auto& s : students) {
        cout << s.name << "\n";
    }
    
    return 0;
}