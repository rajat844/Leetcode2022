class DisjointSet {
    vector<int> parent;

public:
    void makeUnion(int node1, int node2) {
        int parentNode1 = getParent(node1);
        int parentNode2 = getParent(node2);

        if (parentNode1 == parentNode2)
            return;
        else
            parent[parentNode2] = parentNode1;
    }
    DisjointSet(long long n) {
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int getParent(int node) {
        if (parent[node] == node)
            return node;
        else
            return parent[node] = getParent(parent[node]);
    }
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        DisjointSet d(s.size());

        for (int i = 0; i < pairs.size(); i++) {
            if (pairs[i][0] != pairs[i][1])
                d.makeUnion(pairs[i][0], pairs[i][1]);
        }

        vector<int> parent;
        map<int, vector<char>> st;
        for (int i = 0; i < s.size(); i++) {
            int temp = d.getParent(i);
            st[temp].push_back(s[i]);
            parent.push_back(temp);
        }

        for (auto& [key, val] : st) {
            sort(val.begin(), val.end());
        }
        string ans = "";
        for (int i = s.size() - 1; i >= 0; i--) {
            int pNode = parent[i];
            char replacement = st[pNode].back();
            ans += replacement;
            st[pNode].pop_back();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};