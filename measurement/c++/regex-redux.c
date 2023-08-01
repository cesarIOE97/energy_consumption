/* The Computer Language Benchmarks Game
   https://salsa.debian.org/benchmarksgame-team/benchmarksgame/

   contributed by idzeta
*/

#include <iostream>
#include <cassert>
#include <vector>
#include <string>
#include <regex>

using namespace std;

int main()
{
    const char* pattern1[] = {
        "agggtaaa|tttaccct",
        "[cgt]gggtaaa|tttaccc[acg]",
        "a[act]ggtaaa|tttacc[agt]t",
        "ag[act]gtaaa|tttac[agt]ct",
        "agg[act]taaa|ttta[agt]cct",
        "aggg[acg]aaa|ttt[cgt]ccct",
        "agggt[cgt]aa|tt[acg]accct",
        "agggta[cgt]a|t[acg]taccct",
        "agggtaa[cgt]|[acg]ttaccct"
    };

    const char* pattern2[][2] = {
        "tHa[Nt]", "<4>",
        "aND|caN|Ha[DS]|WaS", "<3>",
        "a[NSt]|BY", "<2>",
        "<[^>]*>", "|",
        "\\|[^|][^|]*\\|", "-"
    };

    cout.sync_with_stdio(false);

    cin.seekg(0, ios_base::end);
    size_t read_size = cin.tellg();
    assert(read_size > 0);
    cin.seekg(0, ios_base::beg);

    string str(read_size, '\0');
    cin.read(&str[0], read_size);
    size_t len1 = cin.gcount();
    assert(len1);
    if (len1 < read_size) {
        str.resize(len1);
    }

    string out(str);
    for (size_t i = 0; i < sizeof(pattern2) / sizeof(pattern2[0]); ++i) {
        regex pat(pattern2[i][0]);
        out = regex_replace(out, pat, pattern2[i][1]);
    }

    vector<int> results;
    for (size_t i = 0; i < sizeof(pattern1) / sizeof(pattern1[0]); ++i) {
        regex pat(pattern1[i]);
        sregex_iterator it(out.begin(), out.end(), pat);
        sregex_iterator end;
        int count = 0;
        while (it != end) {
            ++count;
            ++it;
        }
        results.push_back(count);
    }

    for (size_t i = 0; i < sizeof(pattern1) / sizeof(pattern1[0]); ++i) {
        cout << pattern1[i] << " " << results[i] << endl;
    }

    cout << "\n" << len1 << "\n" << out.length() << "\n";
}
