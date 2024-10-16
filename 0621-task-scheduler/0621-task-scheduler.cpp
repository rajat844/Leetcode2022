class Solution {
    struct comp {
        bool operator()(pair<char,int> p1, pair<char,int> p2){
            return p1.second < p2.second; 
        }
    };
    
public:
    int leastInterval(vector<char>& tasks, int n) {
        map<char,int> mp;
        
        for(char task: tasks){
            mp[task]++;
        }
        
        priority_queue<pair<char,int>,vector<pair<char,int>>,comp> pq;
        
        for(const auto&[key,val] : mp){
            pq.push(make_pair(key,val));
        }
        
        queue<pair<char,int>> q;
        int time = 0;
        
        while(!pq.empty() || !q.empty()){
            time++;
            if(!pq.empty()){
                pair<char,int> curr = pq.top();
                pq.pop();
                mp[curr.first]--;
                if(mp[curr.first] > 0){
                    q.push(make_pair(curr.first,time+n));
                }
            }
            
            if(!q.empty() && q.front().second == time){
                pq.push(make_pair(q.front().first,mp[q.front().first]));
                q.pop();
            }
        }
        
        return time;
        
    }
};