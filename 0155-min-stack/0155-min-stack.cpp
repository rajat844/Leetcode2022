class MinStack {
private:
    stack <long> st;
    long minEle;
public:
    
    void push(int val) {
        if(st.size() == 0){
            st.push(val);
            minEle = val;
        }
        else {
            if(val >= minEle) 
                st.push(val);
            else {
                long  x = ((long)val * 2) - minEle;
                minEle = val;
                st.push(x);
            }
        }
    }
    
    void pop() {
        if(st.size() == 0){
            return;
        }
        else if(st.top() > minEle || st.size() == 1){
            st.pop();
        }
        else {
            long x = (minEle * 2) - st.top();
            st.pop();
            minEle = x;
        }
        
    }
    
    int top() {
        if(st.size() == 0) return -1;
        else if(st.top() > minEle || st.size() == 1){
            return st.top();
        }
        else{
            return minEle;
        }
        
    }
    
    int getMin() {
        if(st.size() == 0) return -1;
        else return minEle;
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */