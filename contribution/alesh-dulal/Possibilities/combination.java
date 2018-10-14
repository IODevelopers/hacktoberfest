import java.util.ArrayList;

class Main {

    private static int TARGET_SUM = 100;
    private static int[] VALUES = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

    static ArrayList add(int digit, String sign, ArrayList branches) {
        for (int i = 0; i < branches.size(); i++) {
            branches.set(i, digit + sign + branches.get(i));
        }

        return branches;
    }

    static ArrayList fun(int sum, int number, int index) {
        int digit = Math.abs(number % 10);
        if (index >= VALUES.length) {
            if (sum == number) {
                ArrayList result = new ArrayList();
                result.add(Integer.toString(digit));
                return result;
            }
            else {
                return new ArrayList();
            }
        }

        ArrayList branch1 = fun(sum - number, VALUES[index], index + 1);
        ArrayList branch2 = fun(sum - number, -VALUES[index], index + 1);

        int concatenatedNumber = number >= 0
            ? 10 * number + VALUES[index]
            : 10 * number - VALUES[index];
        ArrayList branch3 = fun(sum, concatenatedNumber, index + 1);

        ArrayList results = new ArrayList();

        results.addAll(add(digit, "+", branch1));
        results.addAll(add(digit, "-", branch2));
        results.addAll(add(digit, "", branch3));

        return results;
    }

    public static void main(String[] args) {
        for (String string : fun(TARGET_SUM, VALUES[0], 1)) {
            System.out.println(string);
        }

    }
}
