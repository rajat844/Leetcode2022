class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;
        
        for(int x : asteroids){
            if(x > 0 ){
                st.push_back(x);
            }
            
            else{
                int prev = 0;
                while(st.size() > 0 && st.back() > 0 && st.back() < abs(x)) {
                    cout << prev << endl;
                    prev = st.back();
                    st.pop_back();
                }
                if(st.size() > 0 && st.back() == abs(x))
                    st.pop_back();
                else if(st.size() == 0 || st.back() < 0)
                    st.push_back(x);
            }
        }
        return st;
    }
};