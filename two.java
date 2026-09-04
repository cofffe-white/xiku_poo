import java.util.Scanner;
public class two {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("me diga um numero entre 10 e 20: ");
        int r = s.nextInt();
        if(r > 10 && r < 20){
            System.out.println("numero certo");
        }
        else{
            System.out.println("incorreto");
        }
    }
}