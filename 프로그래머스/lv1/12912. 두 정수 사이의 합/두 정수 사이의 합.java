class Solution {
    public long solution(int a, int b) {
        long max, min, answer = 0;
        max = a>b ? a : b;
        min = a<b ? a : b;
        
        while(true){
            answer+=min;
            min++;
            if(max<min){
                break;
            }
        }
        
        return answer;
    }
}