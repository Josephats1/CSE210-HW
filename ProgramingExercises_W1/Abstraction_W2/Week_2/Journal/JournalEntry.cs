using System;

public class JournalEntry
{
    // Properties for Date, Prompt, and Response
    public string Date { get; set; }
    public string Prompt { get; set; }
    public string Response { get; set; }

    // Constructor to initialize a JournalEntry
    public JournalEntry(string prompt, string response)
    {
        Date = DateTime.Now.ToString("yyyy-MM-dd");  // Automatically capture the date when the entry is created
        Prompt = prompt;
        Response = response;
    }

    // Override ToString() to display the journal entry in a readable format
    public override string ToString()
    {
        return $"{Date} | Prompt: {Prompt} | Response: {Response}";
    }
}
