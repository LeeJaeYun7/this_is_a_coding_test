import java.util.*; 

public class Main{
  
  public static void main(String[] args){
    
      Scanner sc = new Scanner(System.in);
      int N = sc.nextInt(); 
      int[] coins = {500, 100, 50, 10};
      int ans = 0; 
    
      // coin 배열이 있으니, for문으로 순회하는 것이 좋다. 
      for(Integer coin: coins){
          // ans에 새로 구한 개수를 더해준다. 
          ans += (N/coin);
          // 남은 금액은 바로 N을 현재 coin으로 나눈 나머지 값이다. 
          N %= coin;
      }
    
  }
  
}
