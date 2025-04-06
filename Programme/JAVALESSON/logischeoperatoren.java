public class logischeoperatoren {

    public static void main(String[] args) {
        
        double temp = 20;

        if (temp > 22 && temp < 26) /* && ist ein logischer UND Operator "|| ist das ODER Operator"*/ {System.out.println("Angenehm");}

        else{System.out.println("Entspannt");}


        /* Exclusive ODER Operator */

        boolean jan_wins = false;
        boolean tim_wins = true;

        if (jan_wins ^ tim_wins) /* 2 Booleans miteinander verbinden entweder jan oder tim gewinnt*/

        System.out.println("Richtiges Ergebnis");
        
        else{System.out.println("Da stimmt was nicht!!");}
    }
    
}
