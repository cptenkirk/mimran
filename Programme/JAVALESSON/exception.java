public class exception{

    public static void main(String[] args) {
       
        int zahl = 1;
    int teiler = 0;

    try {
        int divisionErgebnis = zahl / teiler;
        System.out.println("Ergebnis=" + divisionErgebnis);

    } catch (ArithmeticException ex1) {ex1.printStackTrace();}
        
        catch (ArrayStoreException ex2) {ex2.printStackTrace();}

            catch (Exception ex3) {ex3.printStackTrace();}
    }
    

}