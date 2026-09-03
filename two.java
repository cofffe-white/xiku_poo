import java.util.Scanner;
public class two {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("o gustavo é pai? ");
        String r = s.next();
        if( r.equals("sim")){
            System.out.println("o gustavo é pai");
        } else {
            System.out.println("ele nao fez ainda");
        }
    }
}