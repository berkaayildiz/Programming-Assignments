package utils;

import java.util.Scanner;

/**
 * This class contains static methods to get user input.
 * Created to reduce code clutter in the main method.
 */
public final class InputReader
{

    public static int getCarCount(Scanner scanner)
    {
        int numberOfCars = 0;
        boolean validInput = false;
        
        while (!validInput)
        {
            System.out.print("Enter available car count, N=");
            if (scanner.hasNextInt())
            {
                numberOfCars = scanner.nextInt();
                validInput = true;
            }
            else
            {
                System.out.println("\nInvalid input. Please enter an integer.\n");
                scanner.next(); // discard invalid input
            }
        }
        
        return numberOfCars;
    }

    public static int getCustomerCount(Scanner scanner)
    {
        int numberOfCustomers = 0;
        boolean validInput = false;
        
        while (!validInput)
        {
            System.out.print("Enter customer count, k=");
            if (scanner.hasNextInt())
            {
                numberOfCustomers = scanner.nextInt();
                validInput = true;
            }
            else
            {
                System.out.println("\nInvalid input. Please enter an integer.\n");
                scanner.next(); // discard invalid input
            }
        }

        return numberOfCustomers;
    }
}
