// AUTHOR AnindyaPaul akpaul@bu.edu
// AUTHOR ShermanSze ysze@bu.edu
// AUTHOR DiWu wudi@bu.edu
// AUTHOR JianqingGao gaojq@bu.edu
// AUTHOR JiangyuWang jiangyu@bu.edu
// Copyright 2016 Sherman Sze

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <sstream>
#include <algorithm>

using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::ifstream;
using std::unordered_map;

typedef vector<string> vecstr;
typedef unordered_map<char, int> charCount;
typedef unordered_map<int, unordered_map<string, vecstr > > wordDict;

wordDict Dict;

charCount counter(string str) {
    charCount strCharCount;

    for (int i = 0; i < str.length(); i++) {
        strCharCount[str[i]] = count(str.begin(), str.end(), str[i]);
    }

    return strCharCount;
}


bool doesContain(string inputStr, string dictStr) {
    charCount inputCon = counter(inputStr);
    charCount dictCon = counter(dictStr);

    int value;

    for (int i = 0; i < dictStr.length(); i++) {
        charCount::const_iterator it = inputCon.find(dictStr[i]);

        if (it == inputCon.end()) return false;

        value = it->second;

        if (value < dictCon[dictStr[i]]) return false;
    } return true;
}

void print(string word) {
    cout << word << endl;
}



int main(int argc, char const *argv[]) {
    ifstream file(argv[1]);
    string word;

    while (file >> word) {
        string sortedWord = word;
        sort(sortedWord.begin(), sortedWord.end());
        Dict[word.length()][sortedWord].push_back(word);
    }

    file.close();

    while (true) {
        string inputStr;
        int num;

        cin >> inputStr >> num;

        string sortedIn = inputStr;
        sort(sortedIn.begin(), sortedIn.end());

        if (num == 0) {
            return 0;

        } else if (inputStr.length() == num) {
            vecstr strV(Dict[num][sortedIn].begin(), Dict[num][sortedIn].end());
            sort(strV.begin(), strV.end());

            for_each(strV.begin(), strV.end(), print);
            cout << "." << endl;

        } else {
            vecstr result;


            for (auto it = Dict[num].begin(); it != Dict[num].end(); ++it) {
                string dictS = it->first;

                vecstr strVec(Dict[num][dictS].begin(), Dict[num][dictS].end());

                if (doesContain(sortedIn, dictS)) {
                    result.insert(result.end(), strVec.begin(), strVec.end());
                }
            }

            sort(result.begin(), result.end());

            for_each(result.begin(), result.end(), print);

            cout << "." << endl;
        }
    }

    return 0;
}


