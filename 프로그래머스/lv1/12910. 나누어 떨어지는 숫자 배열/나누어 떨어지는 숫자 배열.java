class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        int T = 0;
        
        for(int i=0;i<arr.length;i++){ // 배열 크기 지정
            if(arr[i]%divisor==0){
                T++;
            } 
        }
    
        answer = new int [T]; // 배열 선언
        
        int K = 0; // 조건 부합하는 요소 answer에 넣기
        for(int i=0;i<arr.length;i++){
            if(arr[i]%divisor==0){
                answer[K]=arr[i];
                K++;
            }
        }
        
         for(int i=0;i<answer.length-1;i++){ // 크기대로 조정 
            if(answer[i]>answer[i+1]){
                int temp = answer[i];
                answer[i]=answer[i+1];
                answer[i+1]=temp;
                i=-1;
            } 
        }
        
        if(T==0){
            answer = new int [1];
            answer[0] = -1;
        }
        return answer;
    }
}