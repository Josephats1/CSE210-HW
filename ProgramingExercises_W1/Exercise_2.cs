using System;

class Program
{
    static void Main()
    {
        // Ask for the user's grade percentage
        Console.Write("Enter your grade percentage: ");
        string gradeInput = Console.ReadLine();
        
        // Convert the input to an integer
        int grade = int.Parse(gradeInput);
        
        // Variable to store the letter grade
        string letter = "";
        
        // Determine the letter grade based on the grade percentage
        if (grade >= 90)
        {
            letter = "A";
        }
        else if (grade >= 80)
        {
            letter = "B";
        }
        else if (grade >= 70)
        {
            letter = "C";
        }
        else if (grade >= 60)
        {
            letter = "D";
        }
        else
        {
            letter = "F";
        }

        // Display the grade letter
        Console.WriteLine($"Your letter grade is: {letter}");

        // Determine if the student passed
        if (grade >= 70)
        {
            Console.WriteLine("Congratulations, you passed the course!");
        }
        else
        {
            Console.WriteLine("Sorry, you did not pass. Better luck next time!");
        }
    }
}
