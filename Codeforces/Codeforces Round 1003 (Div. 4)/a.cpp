#include <iostream>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        string w;
        cin >> w;
        w.erase(w.size() - 2);
        cout << w + "i" << "\n";
    }
}
