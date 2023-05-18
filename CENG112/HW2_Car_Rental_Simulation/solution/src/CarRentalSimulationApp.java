import java.util.Scanner;

import classes.Car;
import classes.Customer;

import implementations.ArrayDeque;
import implementations.ArrayList;
import implementations.ArrayQueue;

import interfaces.DequeInterface;
import interfaces.ListInterface;
import interfaces.QueueInterface;

import utils.InputReader;


public class CarRentalSimulationApp
{
    public static void main(String[] args)
    {        
        // Get user input for car count and customer count
        // And check if the input is valid
        Scanner scanner = new Scanner(System.in);
        int numberOfCars = InputReader.getCarCount(scanner);
        int numberOfCustomers = InputReader.getCustomerCount(scanner);
        scanner.close();

        // Create a deque of Car objects
        // And add Car objects to the deque
        DequeInterface<Car> carDeque = new ArrayDeque<Car>(numberOfCars);
        for (int i = 0; i < numberOfCars; i++)
        {
            carDeque.addToBack(new Car());
        }

        // Create a queue of Customer objects
        // And add Customer objects to the queue
        QueueInterface<Customer> customerQueue = new ArrayQueue<Customer>(numberOfCustomers);
        for (int i = 0; i < numberOfCustomers; i++)
        {
            customerQueue.enqueue(new Customer());
        }

        // Create a list for Car objects
        // to keep track of rented cars.
        ListInterface<Car> rentedCarsList = new ArrayList<Car>(numberOfCars);

        System.out.println(); // A space between the input and the simulation

        // ===================== Simulation =====================

        int currentDay = 1;
        // Simulation will continue until there are no more customers left in the queue
        while(!customerQueue.isEmpty())
        {    
            System.out.println("**************" + "Day" + currentDay + "**************");
            
            // If the car deque is not empty, customers will be offered cars
            if (!carDeque.isEmpty())
            {   
                // Showing all of the cars in the deque to customers
                int carDequeSize = carDeque.size();
                for(int i = 0; i < carDequeSize; i++)
                {   
                    if (customerQueue.isEmpty()) // To exit early from the loop if there are no more customers left in the queue
                    {
                        break;
                    }
    
                    Car currentCar = carDeque.removeFront();
                    Boolean isCurrentCarRented = false;
    
                    System.out.println("Current " + currentCar.toString() + " is offering to");
                    
                    // Showing the current car to all of the customers in the queue
                    int customerQueueSize = customerQueue.size();
                    for (int j = 0; j < customerQueueSize; j++)
                    {
                        Customer currentCustomer = customerQueue.dequeue();

                        // If the car is not rented by any customer, show it to the current customer
                        if (!isCurrentCarRented)
                        {   
                            // The case where the customer accepts the car
                            if (currentCustomer.getQualityThreshold() <= currentCar.getQualityScore())
                            {
                                System.out.print("        " + "Current " + currentCustomer.toString());
                                System.out.println("          " + "---accepted");
    
                                currentCar.rentTo(currentCustomer);
                                rentedCarsList.add(currentCar);
    
                                isCurrentCarRented = true;                          
                            }
                            // The case where the customer rejects the car
                            else
                            {
                                System.out.print("        " + "Current " + currentCustomer.toString());
                                System.out.println("          " + "---not accepted");
                                
                                // Reducing the quality threshold of the customer before putting it back to the queue
                                currentCustomer.reduceQualityThreshold();

                                customerQueue.enqueue(currentCustomer);
                            }
                        }
                        // If the car is already rented by a customer, put the customer back to the queue
                        // This block is for protecting the order of the queue
                        else
                        {
                            customerQueue.enqueue(currentCustomer);
                        }
                    }
                    
                    // If the current car is rejected by all of the customers, add it back to the deque
                    if (!isCurrentCarRented && !customerQueue.isEmpty())
                    {   
                        System.out.println("        " + "---not accepted by any customer----");
                        carDeque.addToBack(currentCar);
                    }
                }
                
                System.out.println("All cars have seen");
                
            }
            // If the car deque is empty, show a message to the user
            else
            {
                System.out.println("No cars available for today.");
            }


            // If there are still customers left in the queue, show the current status of the simulation
            if (!customerQueue.isEmpty())
            {
                System.out.println("But there are still customers waiting.");
                
                // Shows currently rented cars if there are any
                if (!rentedCarsList.isEmpty())
                {
                    System.out.println("Rented cars:");

                    for(int i = 0; i < rentedCarsList.size(); i++)
                    {
                        System.out.print("        " + rentedCarsList.get(i).getCarID());
                        System.out.print(" by " + rentedCarsList.get(i).getRentedBy().getCustomerID());
                        System.out.println(" occupancy=" + rentedCarsList.get(i).getOccupancyDaysLeft());
                    }
                }

                // Shows currently available cars if there are any
                if (!carDeque.isEmpty())
                {
                    System.out.println("Available cars:");

                    for (int i = 0; i < carDeque.size(); i++)
                    {
                        Car availableCar = carDeque.removeFront();
                        System.out.println("        " + availableCar.getCarID());
                        carDeque.addToBack(availableCar);
                    }
                }

                // End of the day with preparing for the next day 
                // will only be executed if there are still customers left in the queue.
                // The program will not try to prepare for the next day if there are no more customers left.
                System.out.println("****************" + "End of Day" + "****************:\n");
                currentDay++;
    
                // Decrease the occupancy days left of rented cars by 1 at the end of each day
                // And add the cars that have 0 occupancy days left to the deque back
                for (int i = 0; i < rentedCarsList.size(); i++)
                {
                    Car currentRentedCar = rentedCarsList.get(i);
                    currentRentedCar.decreaseOccupancyDaysLeft();
    
                    if (currentRentedCar.getOccupancyDaysLeft() == 0)
                    {
                        carDeque.addToFront(currentRentedCar);

                        // Removing entries while iterating over list is kinda tricky
                        // So after removing an entry, we need to decrease the i by 1
                        // to avoid skipping the next entry
                        rentedCarsList.remove(i);
                        i--;
                    }
                }
            } 
            // If the customer queue is empty, show a message to the user and exit the simulation
            else
            {
                System.out.println("All customer rent a car.");
            }
        }
    }
}
