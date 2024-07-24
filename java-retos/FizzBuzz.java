import java.util.Scanner;

/**
 * FizzBuzz
 */
public class FizzBuzz {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println(entrada.getClass().getSimpleName());
        
        String numero_String = entrada.nextLine();
        System.out.println(numero_String.getClass().getSimpleName());

        int numero = Integer.parseInt(numero_String);
        System.out.println(((Object)numero).getClass().getSimpleName());

        entrada.close();
        for (int i=1; i<=numero; i++){
            boolean multiploDe3 = (i%3==0);
            boolean multiploDe5 = (i%5==0);
            boolean multiploDe3y5 = multiploDe3 && multiploDe5;
        
            if(multiploDe3y5){System.out.println("fizzbuzz");}
            else if(multiploDe3){System.out.println("fizz");}
            else if(multiploDe5){System.out.println("buzz");}
            else {System.out.println(i);}
        }
    }
}