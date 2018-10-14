import java.util.Scanner;
class Fibonacci{
	public static void main(String args[]){
		int i;
		int num1=0;
		int num2=1;
		int num3;
		Scanner SC = new Scanner(System.in);
		System.out.println("Enter number upto which you need fibonacci:");
		
		int number = SC.nextInt();
		System.out.println("You Entered: "+number);

		for (i=2; i<=number; i++) {
			num3 = num1+num2;
			System.out.println(num3);
			num1=num2;
			num2=num3;
		}
	}
}
