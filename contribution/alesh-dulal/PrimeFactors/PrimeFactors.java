import java.util.Scanner;
class PrimeFactors{
	public static void main(String args[]){
		Scanner SC = new Scanner(System.in);
		System.out.println("Enter number to find Prime Factors:");
		int number = SC.nextInt();
		System.out.println("The number you enter is:"+number);
		System.out.println("The Prime Factors are:");

		for(int i=2; i<=number; i++){
			if(number%i==0){
				System.out.println(i+" ");
				number = number/i;
			}//if ends
		}//for loop ends
		if(number <= 1){
			System.out.println(number);
		}
	}
}
