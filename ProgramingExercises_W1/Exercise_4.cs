using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Create a list to store the numbers
        List<int> numbers = new List<int>();
        int input;

        // Prompt the user to enter numbers
        Console.WriteLine("Enter a list of numbers, type 0 when finished.");

        // Collect numbers until the user enters 0
        do
        {
            Console.Write("Enter number: ");
            input = int.Parse(Console.ReadLine());

            if (input != 0)
            {
                numbers.Add(input);
            }
        } while (input != 0);

        // Compute the sum of the numbers
        int sum = 0;
        foreach (int number in numbers)
        {
            sum += number;
        }

        // Compute the average of the numbers
        double average = (numbers.Count > 0) ? (double)sum / numbers.Count : 0;

        // Find the maximum number in the list
        int maxNumber = numbers.Count > 0 ? numbers[0] : 0;
        foreach (int number in numbers)
        {
            if (number > maxNumber)
            {
                maxNumber = number;
            }
        }

        // Find the smallest positive number (closest to zero)
        int smallestPositive = int.MaxValue;  // Initialize to a large number
        foreach (int number in numbers)
        {
            if (number > 0 && number < smallestPositive)
            {
                smallestPositive = number;
            }
        }

        // Sort the list
        numbers.Sort();

        // Display the results
        Console.WriteLine($"The sum is: {sum}");
        Console.WriteLine($"The average is: {average}");
        Console.WriteLine($"The largest number is: {maxNumber}");
        
        if (smallestPositive != int.MaxValue)
        {
            Console.WriteLine($"The smallest positive number is: {smallestPositive}");
        }
        else
        {
            Console.WriteLine("No positive numbers were entered.");
        }

        // Display the sorted list
        Console.WriteLine("The sorted list is:");
        foreach (int number in numbers)
        {
            Console.WriteLine(number);
        }
    }
}