using System;

class Program
{
    // Function to display a welcome message
    static void DisplayWelcome()
    {
        Console.WriteLine("Welcome to the Program!");
    }

    // Function to prompt the user for their name
    static string PromptUserName()
    {
        Console.Write("Please enter your name: ");
        return Console.ReadLine();
    }

    // Function to prompt the user for their favorite number
    static int PromptUserNumber()
    {
        Console.Write("Please enter your favorite number: ");
        int favoriteNumber;
        // Ensure valid input
        while (!int.TryParse(Console.ReadLine(), out favoriteNumber))
        {
            Console.Write("Invalid input. Please enter a valid number: ");
        }
        return favoriteNumber;
    }

    // Function to square the number
    static int SquareNumber(int number)
    {
        return number * number;
    }

    // Function to display the result
    static void DisplayResult(string name, int squaredNumber)
    {
        Console.WriteLine($"{name}, the square of your number is {squaredNumber}");
    }

    // Main function that calls other functions
    static void Main()
    {
        // Step 1: Display the welcome message
        DisplayWelcome();

        // Step 2: Get user name
        string userName = PromptUserName();

        // Step 3: Get user favorite number
        int favoriteNumber = PromptUserNumber();

        // Step 4: Calculate the square of the number
        int squaredNumber = SquareNumber(favoriteNumber);

        // Step 5: Display the result
        DisplayResult(userName, squaredNumber);
    }