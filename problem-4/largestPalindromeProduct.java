import java.util.ArrayList;
import java.util.Collections;

public class largestPalindromeProduct {
    public static void main(String[] args) {
        int a = 0;
        int b = 0;
        int c = 0;
        ArrayList<Integer> palindromes = new ArrayList<Integer>();
        while (a < 999) {
            c = a + b;
            if (String.valueOf(c) == String.valueOf(reverseNumber(c))) {
                palindromes.add(c);
            }
        }
        System.out.println(Collections.max(palindromes));
    }
    public static int reverseNumber(int i) {
        int rev = 0;
        while(i != 0) {
            int digit = i % 10;
            rev = rev * 10 + digit;
            i /= 10;
         }
        return rev;
    }
}