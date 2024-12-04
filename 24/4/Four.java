import java.util.Scanner;
import java.util.ArrayList;

public class Four {
    private static int l, h;
    private static int count = 0;
    static ArrayList<String> m = new ArrayList<>();

    static char getChar(int i, int j) {
        return m.get(j).charAt(i);
    }

    static void right(int i, int j) {
        if (i + 3 >= l) {
            return;
        }
        if (m.get(j).substring(i,i+4).equals("XMAS")){
            count++;
        }
    }

    static void left(int i, int j) {
        if (i - 3 <= -1) {
            return;
        }
        if (m.get(j).substring(i-3,i+1).equals("SAMX")){
            count++;
        }
    }

    static void up(int i, int j) {
        if (j - 3 <= -1) {
            return;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i, j - 1));
        sb.append(getChar(i, j - 2));
        sb.append(getChar(i, j - 3));
        if (sb.toString().equals("XMAS")){
            count++;
        }
    }

    static void down(int i, int j) {
        if (j + 3 >= h) {
            return;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i, j + 1));
        sb.append(getChar(i, j + 2));
        sb.append(getChar(i, j + 3));
        if (sb.toString().equals("XMAS")){
            count++;
        }
    }

    static void nw(int i, int j) {
        if ((i - 3 <= -1) || (j - 3 <= -1)) {
            return;
        }

        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i - 1, j - 1));
        sb.append(getChar(i - 2, j - 2));
        sb.append(getChar(i - 3, j - 3));
        if (sb.toString().equals("XMAS")){
            count++;
        }
    }

    static void sw(int i, int j) {
        if ((i - 3 <= -1) || (j + 3 >= h)) {
            return;
        }

        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i - 1, j + 1));
        sb.append(getChar(i - 2, j + 2));
        sb.append(getChar(i - 3, j + 3));
        if (sb.toString().equals("XMAS")){
            count++;
        }
    }

    static void ne(int i, int j) {
        if ((i + 3 >= l) || (j - 3 <= -1)) {
            return;
        }

        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i + 1, j - 1));
        sb.append(getChar(i + 2, j - 2));
        sb.append(getChar(i + 3, j - 3));
        if (sb.toString().equals("XMAS")){
            count++;
        }
    }

    static void se(int i, int j) {
        if ((i + 3 >= l) || (j + 3 >= h)) {
            return;
        }

        StringBuilder sb = new StringBuilder();
        sb.append(getChar(i, j));
        sb.append(getChar(i + 1, j + 1));
        sb.append(getChar(i + 2, j + 2));
        sb.append(getChar(i + 3, j + 3));
        if (sb.toString().equals("XMAS")){
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
                right(i, j);
                left(i, j);
                up(i, j);
                down(i, j);
                nw(i, j);
                sw(i, j);
                ne(i, j);
                se(i, j);
            }
        }
        System.out.println(count);
    }
}
