using System;

class Program
{
    static void Main()
    {
        Reference reference = new Reference("John", 3, 16);
        Scripture scripture = new Scripture(reference, 
            "For God so loved the world that he gave his only begotten Son, " +
            "that whosoever believeth in him should not perish, but have everlasting life.");

        Console.Clear();
        Console.WriteLine("Scripture Memorization Game");
        Console.WriteLine("===========================\n");

        while (true)
        {
            Console.Clear();
            Console.WriteLine(scripture.GetDisplayText());
            Console.WriteLine("\nPress Enter to hide more words, or type 'quit' to exit.");

            string input = Console.ReadLine();
            if (input.ToLower() == "quit") break;

            scripture.HideRandomWords(3); // Hide 3 words at a time

            if (scripture.IsCompletelyHidden())
            {
                Console.Clear();
                Console.WriteLine("You have fully memorized the scripture!\n");
                Console.WriteLine(scripture.GetDisplayText());
                break;
            }
        }

        Console.WriteLine("\nThank you for using the Scripture Memorizer Program!");
    }
}
