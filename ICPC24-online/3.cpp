#include <stdio.h>
#include <limits.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int s1, f1, h1, s2, f2, h2, s3, f3, h3;
        scanf("%d %d %d %d %d %d %d %d %d", &s1, &f1, &h1, &s2, &f2, &h2, &s3, &f3, &h3);

        int s = s1 + s2 + s3;
        int f = f1 + f2 + f3;
        int h = h1 + h2 + h3;

        int mn = INT_MAX;
        char best[4];

        char perms[6][4] = {"FHS", "FSH", "HFS", "HSF", "SFH", "SHF"};

        for (int i = 0; i < 6; i++) {
            int moves = 0;
            moves += s - (perms[i][0] == 'S' ? s1 : perms[i][1] == 'S' ? s2 : s3);
            moves += f - (perms[i][0] == 'F' ? f1 : perms[i][1] == 'F' ? f2 : f3);
            moves += h - (perms[i][0] == 'H' ? h1 : perms[i][1] == 'H' ? h2 : h3);

            if (moves < mn) {
                mn = moves;
                strcpy(best, perms[i]);
            }
        }

        printf("%s %d\n", best, mn);
    }

    return 0;
}