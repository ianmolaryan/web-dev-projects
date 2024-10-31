import java.math.*;
import java.util.*;

public class ShanksBot
{
    public static int countRepeatingDecimalLength(int input)
    {
        int precision = input * 2;  
        BigDecimal numerator = BigDecimal.ONE;
        BigDecimal denominator = new BigDecimal(input);
        MathContext mc = new MathContext(precision);
        String result = numerator.divide(denominator, mc).toString();
        String decimalPart = result.split("\\.")[1];

        for (int length = 1; length <= decimalPart.length() / 2; length++)
        {
            String pattern = decimalPart.substring(0, length);
            boolean isRepeating = true;

            for (int start = length; start + length <= decimalPart.length(); start += length)
            {
                if (!decimalPart.substring(start, start + length).equals(pattern))
                {
                    isRepeating = false;
                    break;
                }
            }

            if (isRepeating)
            {
                return length;
            }
        }
        return 0;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        for(int i=0; i>=0; i++)
        {
            System.out.print("Enter a prime number: ");
            int prime = sc.nextInt();
            long startTime = System.nanoTime();
            System.out.println("Length of repeating part: " + countRepeatingDecimalLength(prime));
            long endTime = System.nanoTime();
            double durationInSeconds = (endTime - startTime) / 1_000_000_000.0;
            try
            {
                Thread.sleep(1500); 
            }
            catch (InterruptedException e)
            {
                System.out.println("Program corrupted, please try once again!");
            }
            System.out.println("Execution time: " + durationInSeconds + " seconds or "+(endTime - startTime)+" nanoseconds.");
        }
    }
}