class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        vector<int> notes(3,0);
        
        for(int i = 0; i < bills.size(); i++){
            if(bills[i] == 20){
                if(notes[0] != 0 && notes[1] != 0){
                    notes[0]--;
                    notes[1]--;
                    notes[2]++;
                }
                else if(notes[0] >= 3){
                    notes[0] -= 3;
                    notes[2]++;
                }
                else {
                    return false;
                }
            }
            else if(bills[i] == 10){
                if(notes[0] != 0){
                    notes[0]--;
                    notes[1]++;
                }
                else{
                    return false;
                }
            }
            else {
                notes[0]++;
            }
        }
        
        return true;
        
    }
};