import java.util.HashSet;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class CD {
  public static void main(String[] args) throws Exception {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    HashSet<String> jackscds = new HashSet<String>(1000000);
    String[] parts = scan.readLine().split(" ");
    int n = Integer.parseInt(parts[0]);
    int m = Integer.parseInt(parts[1]);
    //System.out.println(n);
    //System.out.println(m);

    while(true){
      for (int i = 0; i < n; i++) {
        jackscds.add(scan.readLine());
      }

      int sum = 0;
      for (int i = 0; i < m; i++) {
        String cd = scan.readLine();
        if (jackscds.contains(cd)) {
          sum++;
        }
      }
      System.out.println(sum);
      parts = scan.readLine().split(" ");
      n = Integer.parseInt(parts[0]);
      m = Integer.parseInt(parts[1]);
      if (n == 0 && m == 0) {
        break;
      }
      jackscds.clear();
    }
  }
}
