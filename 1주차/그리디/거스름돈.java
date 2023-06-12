import java.util.*; 

public class Main{
  
  public static void main(String[] args){
    
      Scanner sc = new Scanner(System.in);
      int N = sc.nextInt(); 
      int[] arr = {500, 100, 50, 10};
      int pos = 0;   
      int ans = 0; 
    
      while(true){
         
         // pos위치에 있는 동전으로 나눌 수 있는 개수를 구한다. 
         int cnt = N / arr[pos];
         // 현재 금액에서, 해당 동전 금액*동전 개수를 빼준다.
         N -=  arr[pos]*cnt; 
         // 개수를 전체 개수에 합해준다. 
         ans += cnt; 
         // pos를 1 더해준다. 
         pos++; 
         // N이 0이 되거나, 즉 남은 금액이 없거나, pos가 4가 되면 break를 한다. 
         if(N == 0 || pos ==4){
           break;
         }
      }
      
      System.out.println(ans); 
    
  }
  
  
  
}
