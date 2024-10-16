class Twitter {
private:
    int history=0;
    unordered_map<int, unordered_set<int>> following;
    unordered_map<int, vector<pair<int,int>>> tweets;
    
public:
    Twitter() {
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({history,tweetId});
        history++;
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> ans;
        priority_queue<pair<int,int>> pq;
        
        for(auto tweet : tweets[userId]){
            pq.push(tweet);
        }
        
        for(auto followee : following[userId]){
            for(auto tweet: tweets[followee]){
                pq.push(tweet);
            }
        }
        int sz = pq.size();
        int n = min(10,sz);
        for(int i=0; i<n;i++){
            int a = pq.top().second; pq.pop();
            ans.push_back(a);
        }
        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        
        following[followerId].insert(followeeId);
        
    }
    
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
        
        
    }
};