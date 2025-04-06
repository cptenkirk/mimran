import java.util.Arrays;


public class ausgabedatentyp2 {
    public static void main(String[] args) {
      
      
        int[] meinArray = {2,1,7,3,4,9};
        sortArrayFromIndex(meinArray);
        getValues(meinArray);}

        
            public static void sortArrayFromIndex(int[] meinArray) {Arrays.sort(meinArray, 2,6);}

            public static void getValues(int[] meinArray) {
                for (int elem : meinArray) {System.out.print(elem + "\t");}
            }
        
        


    
    
}
