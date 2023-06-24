class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int [] num = new int [10]; // 10크기 배열 선언
        
        for(int i=0;i<numbers.length;i++){ // numbers의 숫자를 num의 번호로 
            int n = numbers[i];
            num[n]=-1;
        }
        
        for(int i=0;i<=9;i++){
            System.out.println(num[i]);
            if(num[i]==0){
                answer+=i;
            }
            
        }
        return answer;
    }
}