class Solution {
    bool isVowel(char x) {
        if (x == 'a' || x == 'i' || x == 'e' || x == 'o' || x == 'u')
            return true;
        return false;
    }

    long long atMostK(string& word, int k) {
        map<char, int> vowels;
        int consonantsCount = 0;

        int left = 0;
        long long ans = 0;

        for (int right = 0; right < word.size(); right++) {
            if (isVowel(word[right])) {
                vowels[word[right]] += 1;
            } else {
                consonantsCount += 1;
            }

            while (vowels.size() == 5 && consonantsCount > k) {
                if (isVowel(word[left])) {
                    vowels[word[left]] -= 1;
                    if (vowels[word[left]] == 0)
                        vowels.erase(word[left]);
                } else
                    consonantsCount -= 1;

                left += 1;
            }
            ans += right - left + 1;
        }

        return ans;
    }

public:
    long long countOfSubstrings(string word, int k) {
        return atMostK(word, k) - atMostK(word, k - 1);
    }
};