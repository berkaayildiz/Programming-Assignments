package classes;

import java.util.Random;
import java.text.DecimalFormat;

public final class Car
{
    private String carID;
    private double qualityScore;
    private int occupancyDaysLeft;
    private Customer rentedBy;

    private static int numberOfCarsCreated = 0; // static variable to keep track of the number of cars created

    public Car()
    {
        carID = "car" + numberOfCarsCreated;

        Random random = new Random();
        double randomNumber = 1 + (random.nextDouble() * 2);      // generates a random number between 1 and 3
        qualityScore = Math.round(randomNumber * 100.0) / 100.0; // rounds to two decimal places
        
        occupancyDaysLeft = 0;
        rentedBy = null;

        numberOfCarsCreated++;
    }

    public String getCarID()
    {
        return carID;
    }

    public double getQualityScore()
    {
        return qualityScore;
    }

    public int getOccupancyDaysLeft()
    {
        return occupancyDaysLeft;
    }

    public Customer getRentedBy()
    {
        return rentedBy;
    }

    public void setOccupancyDaysLeft(int occupancyDaysLeft)
    {
        this.occupancyDaysLeft = occupancyDaysLeft;
    }

    public void decreaseOccupancyDaysLeft()
    {
        occupancyDaysLeft--;
        
        if (occupancyDaysLeft == 0)
        {
            rentedBy = null;
        }
    }

    public String rentTo(Customer customer)
    {
        rentedBy = customer;
        setRandomOccupancyDaysLeft();

        return (carID + " by" + rentedBy + " occupancy=" + occupancyDaysLeft);
    }

    public String toString()
    {
        DecimalFormat homeworkDecimalFormat = new DecimalFormat("#,##0.00");
        return (carID + " quality=" + homeworkDecimalFormat.format(qualityScore));
    }
    
    private void setRandomOccupancyDaysLeft()
    {
        Random random = new Random();
        occupancyDaysLeft = 1 + random.nextInt(5); // generates a random number between 1 and 5
    }
}
