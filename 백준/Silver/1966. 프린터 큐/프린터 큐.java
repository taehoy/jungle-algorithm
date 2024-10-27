import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while(T-- >0){
            LinkedList<int[]> q = new LinkedList<>();
            int cnt = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken()); // 문서 개수
            int M = Integer.parseInt(st.nextToken()); // 타겟 순서

            // 큐에 문서 넣기 [순서, 중요도]

            st = new StringTokenizer(br.readLine());

            for(int i=0; i<N; i++){
                q.offer(new int[]{i, Integer.parseInt(st.nextToken())});
            }

            // 큐가 빌떄까지 반복
            while(!q.isEmpty()){

                // 큐의 맨 앞보다 큰 중요도가 있는 경우
                int[] front = q.poll();
                boolean flag = true;

                // 순회하면서 더 큰 중요도 찾기
                for(int i=0; i<q.size(); i++){
                    if(front[1] < q.get(i)[1]){
                        // 있는 경우 가장 큰 중요도 이전 모두뒤로 보내기

                        q.offer(front);
                        for(int j=0; j<i; j++){
                            q.offer(q.poll());
                        }
                        flag = false;

                        break;
                    }
                }

                if(flag == false){
                    continue;
                }

                cnt++;
                // 없는 경우 내가 찾는 문서인지 확인
                if(front[0] == M) {
                    break;
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.println(sb);
    }
}
