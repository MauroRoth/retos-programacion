import java.util.Arrays;

public class Anagrama {
    private static String ordenaPalabra(String palabra){
        char[] caracteres = palabra.toCharArray();
        Arrays.sort(caracteres);
        String nueva_palabra = new String(caracteres);
        return nueva_palabra;
    }
    private static boolean anagrama(String palabra1, String palabra2){
        String n_palabra1 = ordenaPalabra(palabra1);
        String n_palabra2 = ordenaPalabra(palabra2);
        if (n_palabra1==n_palabra2){
            return true;
        }
        return false;

    }
    public static void main(String[] args) {
        System.out.println(anagrama("dabc","Alberto"));
    }
    
}
