
import java.util.LinkedList;

public class meinezahl {

    public static void main(String[] args) {
        
        int zahl = 1;

        switch (zahl){

            case 0 : System.out.print("Meine Zahl ist 0");
            break;
            case 1 : System.out.print("Meine Zahl ist 1");
            
            case 2 : System.out.print("Meine Zahl ist 1 oder 2");
            break;
            default : System.out.print("Meine Zahl entspricht nicht");
            
        }

        LinkedList linkedList = new LinkedList<>();

        linkedList.add("a");
        linkedList.add("b");
        linkedList.add("c");
        System.out.println(linkedList);
    }




    
}
