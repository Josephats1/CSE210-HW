using System;

class Program
{
    static void Main()
    {
        bool playAgain = true;

        while (playAgain)
        {
            // Create a Random object to generate a magic number
            Random randomGenerator = new Random();
            int magicNumber = randomGenerator.Next(1, 101);  // Random number between 1 and 100

            int guess;
            int guessCount = 0;  // Track number of guesses

            // Start a loop that continues until the guess is correct
            do
            {
                // Ask for a guess
                Console.Write("What is your guess? ");
                guess = int.Parse(Console.ReadLine());
                guessCount++;

                // Check if the guess is correct, too high or too low
                if (guess < magicNumber)
                {
                    Console.WriteLine("Higher");
                }
                else if (guess > magicNumber)
                {
                    Console.WriteLine("Lower");
                }
                else
                {
                    Console.WriteLine("You guessed it!");
                    Console.WriteLine($"It took you {guessCount} guesses.");
                }

            } while (guess != magicNumber);  // Repeat until the guess is correct

            // Ask the user if they want to play again
            Console.Write("Do you want to play again? (yes/no): ");
            string response = Console.ReadLine().ToLower();

            if (response != "yes")
            {
                playAgain = false;
                Console.WriteLine("Thanks for playing!");
            }
        }
    }
}
