class Solution {
    long cars = 0;
    public long minimumFuelCost(int[][] roads, int seats) {
        HashMap<Integer,ArrayList<Integer>> st = new HashMap<Integer,ArrayList<Integer>>();
        
        for(int i = 0; i<roads.length; i++){
            st.putIfAbsent(roads[i][0],new ArrayList<Integer>());
            st.get(roads[i][0]).add(roads[i][1]);
            st.putIfAbsent(roads[i][1],new ArrayList<Integer>());
            st.get(roads[i][1]).add(roads[i][0]);
        }
        
        long pass = travel(st,seats,0,-1);
        return cars;
    }
    
    public long travel(HashMap<Integer,ArrayList<Integer>>st, int seats, int node, int parent){
        long pas = 1;
        if(st.get(node) != null){
        for(Integer x :st.get(node)){
            if(x != parent){
                pas += travel(st,seats,x,node);
            }
        }}
        if(node != 0) cars += (pas + seats - 1)/seats;
        return pas;
    }
}