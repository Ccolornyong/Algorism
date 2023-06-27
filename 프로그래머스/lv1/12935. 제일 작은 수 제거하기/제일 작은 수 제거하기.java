import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    int[] answer = {};
    public int[] solution(int[] arr) {
        int min = arr[0];
        for(int i=0;i<arr.length;i++){
            if(min>arr[i]){
                min=arr[i];
            }
        }
        
        List<Integer> list = new ArrayList<>();
        
       for(int i=0;i<arr.length;i++){
            if(min<arr[i]){
                list.add(arr[i]);
            }
        }
        
        if(list.size()!=0){
            answer = new int[list.size()];
            for(int i=0;i<list.size();i++){
            answer[i]=list.get(i).intValue();
            }
            } else{
            answer = new int [1];
            answer[0]=-1;
        }
        
        return answer;
    }
}