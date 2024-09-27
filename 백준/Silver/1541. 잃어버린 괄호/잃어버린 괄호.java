import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int sum = 0;

        // '-'기준으로 나누기
        String[] arr = s.split("-");


        for(int i=0; i<arr.length; i++){
            String[] arr2 = arr[i].split("\\+");
            for(int j =0; j<arr2.length; j++){
                if(i == 0){
                    sum += Integer.parseInt(arr2[j]);
                } else {
                    sum -= Integer.parseInt(arr2[j]);
                }
            }
        }

        System.out.println(sum);

    }
}
