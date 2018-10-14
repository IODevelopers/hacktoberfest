class Fibo4Million{
	public static void main(String args[]){
		int num1=0, num2=1, num3, i, result = 0;

		while(num1 <= 4000000){
			num3 = num1+num2;
			num1=num2; num2=num3;

			if(num3 % 2 == 0){
				result += num3;
			}
		}
		System.out.println(result);
	}
}