import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    // 윤년 구하기
		
		int A = Integer.parseInt(br.readLine());
		
		if (A % 4 == 0 && A % 100 != 0 || A % 400 == 0) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}
