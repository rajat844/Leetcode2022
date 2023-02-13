class Solution {
    long cars = 0;
    public long minimumFuelCost(int[][] roads, int seats) {
        Map<Integer,ArrayList<Integer>> st = new HashMap<>();
        
        for(int[] road : roads){
            st.computeIfAbsent(road[0],k -> new ArrayList<Integer>()).add(road[1]);
            st.computeIfAbsent(road[1],k -> new ArrayList<Integer>()).add(road[0]);
        }
        
        travel(0,-1,seats,st);
        return cars;
    }
    
    public long travel(int node, int parent, int seats, Map<Integer,ArrayList<Integer>> st){
        int pas = 1;
        if(!st.containsKey(node)) return pas;
        
        for (int x : st.get(node)){
            if(x != parent) pas += travel(x,node,seats,st);
        }
        
        if(node != 0) cars += Math.ceil((double)pas / seats);
        
        return pas;
    }
}
