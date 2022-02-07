// 알람 시계

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] time = br.readLine().split(" ");
		int A = Integer.parseInt(time[0]);
		int B = Integer.parseInt(time[1]);
		
		if (B < 45) {
			if (A == 0) {
				A = 23;
			} else {
				A--;
			}
			B = 60 - 45 + B;
		} else {
			B = B - 45;
		}
		System.out.print(A + " " + B);
	}
}
