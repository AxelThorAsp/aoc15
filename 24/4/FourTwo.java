import java.util.Scanner;
import java.util.ArrayList;

public class FourTwo {
    private static int l, h;
    private static int count = 0;
    static ArrayList<String> m = new ArrayList<>();

    static char getChar(int i, int j) {
        return m.get(j).charAt(i);
    }

    static void check(int i, int j) {
        if (!(getChar(i, j) == 'A')){
            return;
        }
        if ((i + 1 >= l) || (i - 1 <= -1) || (j + 1 >= h) || (j - 1 <= -1)) {
            return;
        }
        StringBuilder sb = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        sb.append(getChar(i - 1, j - 1));  // nw
        sb.append(getChar(i, j)); 
        sb.append(getChar(i + 1, j + 1)); // se
        String st1 = sb.toString();

        sb2.append(getChar(i - 1, j + 1));  // sw
        sb2.append(getChar(i, j)); 
        sb2.append(getChar(i + 1, j - 1));  // ne
        String st2 = sb2.toString();
        if ((st2.equals("MAS") || st2.equals("SAM")) && (st1.equals("MAS") || st1.equals("SAM"))){
                count++;
            }

    }

    public static void main(String[] args) {
        final Scanner sc = new Scanner(System.in);
        String line;
        while(sc.hasNext()){
            line = sc.nextLine();
            m.add(line);
        }
        l = m.get(0).length();
        h = m.size();
        for (int j = 0; j < h; j++){
            for (int i = 0; i < l; i++){
                check(i, j);
            }
        }
        System.out.println(count);
    }
}