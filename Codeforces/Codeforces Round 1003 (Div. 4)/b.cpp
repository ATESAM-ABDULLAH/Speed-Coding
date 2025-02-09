#include <iostream>
#include <string>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        bool ok = false;
        for (int i = 0; i < (int)s.size() - 1; i++){
            if(s[i] == s[i+1]) { ok = true; break; }
        }
        cout << (ok ? 1 : (int)s.size()) << "\n";
    }
    return 0;
}
