import static java.lang.System.out;

public class ifelse {
         public static void main(String[] args) {

            int number = 5;
          
            
            if(number == 5) /* == ist ein vergleich der wahr oder falsch zurückgibt auch eine != Abfrage ist möglich der die Ungleichheit prüft*/ 
            
            // möglich Prüfungen "< kleiner als 5""  > größer als 5""  <= kleiner gleich 5""   >= größer gleich 5"

            { 

                out.println("Nummer ist gleich 5");
            }

            else{out.println("Nummer ist ungleich 5");}


        
        boolean erhoehen = (number < 5);

        if(erhoehen){number += 3; /* += ist gleich 3 */ out.println(number); }

        else{out.println(number);}   
       

        


        


    
}
}