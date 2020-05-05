public class largestPalindromeProduct {
    public static void main(String[] args) {
        int a = 999;
        int b = 999;
        long biggest = 0;

        for (int bb = b; bb > 0; bb--)
        {
            for (int aa = a; aa > 0; aa--)
            {
                if (reverseNumber(aa*bb))
                {
                    if ( aa*bb > biggest )
                    {
                        biggest = aa*bb;
                    }
                }
            }
        }
    System.out.println(biggest);
}

    static boolean reverseNumber(int num) {
        int orig = num;
        int sum=0,r;
        
	    while(num!=0) {
	        r=num%10;
	        sum=(sum*10)+r;
	        num/=10;	
        }
        if (orig == sum) {
            return true;
        }
        else {
            return false;
        }
	}
}