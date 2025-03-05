using System;

class Program
{
    static void Main()
    {
        // Step 1: Ask for the user's first name
        Console.Write("What is your first name? ");
        string firstName = Console.ReadLine();  // Read the user's first name

        // Step 2: Ask for the user's last name
        Console.Write("What is your last name? ");
        string lastName = Console.ReadLine();  // Read the user's last name

        // Step 3: Display the name in the required format
        Console.WriteLine($"Your name is {lastName}, {firstName} {lastName}.");
    }
}
