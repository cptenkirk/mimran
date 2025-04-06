import static java.lang.System.out;

public class party {

    public static void main(String[] args) {
        
        int guests = 11;
        guests = guests - 5; //absagen  
        guests = guests + 1; //zusagen

        String text = "Gaeste angemeldet: ";

        System.out.println(text + guests);

        if (guests < 11)

        out.printf("%d Gaeste sind unzureichend", guests);

        else{out.printf("Die Party ist startklar");}


    }


    
    
}
