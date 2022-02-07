// A+B - 3

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int A = Integer.parseInt(br.readLine());
		int[] result = new int[A];
		
		for(int i=0; i<A; i++) {
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			result[i] = a + b;
		}
		
		for (int i=0; i<result.length; i++) {
			System.out.println(result[i]);
		}
	}
}
