package classes;

import java.text.DecimalFormat;
import java.util.Random;

public final class Customer
{
    private String customerID;
    private double qualityThreshold;
    
    private static int numberOfCustomersCreated = 0; // static variable to keep track of the number of customers created

    public Customer()
    {
        customerID = "cust" + numberOfCustomersCreated;

        Random random = new Random();
        double randomNumber = 1 + (random.nextDouble() * 2);          // generates a random number between 1 and 3
        qualityThreshold = Math.round(randomNumber * 100.0) / 100.0; // rounds to two decimal places

        numberOfCustomersCreated++;
    }

    public String getCustomerID()
    {
        return customerID;
    }

    public double getQualityThreshold()
    {
        return qualityThreshold;
    }

    public void reduceQualityThreshold()
    {
        qualityThreshold *= 0.9;
    }

    public String toString()
    {   
        DecimalFormat homeworkDecimalFormat = new DecimalFormat("#,##0.00");
        return (customerID + " threshold=" + homeworkDecimalFormat.format(qualityThreshold));
    }
}
