import java.util.*;
class Fill{
public static void main(String[] args){
	String[] Array1 = new String[] {"Hello","HI","Mora","MOMO"};
    String[] Array2 = new String[] {"HI", "Mora"};
    boolean contains = false;
    List<String> results = new ArrayList<String>();


    for(int i=0; i<Array1.length; i++) {
        for(int j=0; j<Array2.length; j++) {
            if(Array1[i]==Array2[j]) {
                contains = true;
                break;
            }
        }
        if(!contains) {
            results.add(Array1[i]);
        }
        else{
            contains = false;
        }
    }

    System.out.println(results);
}
}
