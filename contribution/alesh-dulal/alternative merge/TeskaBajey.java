import java.util.*;
import java.io.*;  
class ListMerge{
	public static ArrayList merge(ArrayList a, ArrayList b) {
    int c1 = 0, c2 = 0;
    ArrayList<String> res = new ArrayList<String>();

	    while(c1 < a.size() || c2 < b.size()) {
	        if(c1 < a.size())
	            res.add((String) a.get(c1++));
	        if(c2 < b.size())
	            res.add((String) b.get(c2++));
	    }
    	return res;
	}
	public static void main(String[] args){
		ArrayList<String> list1 = new ArrayList<String>();
			list1.add("A");
			list1.add("B");
			list1.add("C");
		ArrayList<String> list2 = new ArrayList<String>();
			list2.add("1");
			list2.add("2");
			list2.add("3");
		ListMerge LM = new ListMerge();
		System.out.println(LM.merge(list1, list2));
	}
}
