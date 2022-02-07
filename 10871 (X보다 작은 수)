// X보다 작은 수

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int arr[] = new int[Integer.parseInt(st.nextToken())];
		int num = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		
		for (int i=0; i<arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i=0; i<arr.length; i++) {
			if (arr[i] < num) {
      // 뒤에 공백을 같이 넣어주어야 오류 안 남
				bw.write(arr[i] + " ");
			}
		}
		bw.flush();
		bw.close();
	}
}
