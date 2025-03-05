// Job.cs
public class Job
{
    // Member variables (attributes)
    public string _jobTitle;
    public string _company;
    public int _startYear;
    public int _endYear;

    // Constructor to initialize Job object public Job(string jobTitle, string company, int startYear, int endYear)
     public Job(string jobTitle, string company, int startYear, int endYear)
    {
        _jobTitle = jobTitle;
        _company = company;
        _startYear = startYear;
        _endYear = endYear;
    }

    // Method to display job information
    public void DisplayJobDetails()
    {
        Console.WriteLine($"{_jobTitle} ({_company}) {_startYear}-{_endYear}");
    }
}
