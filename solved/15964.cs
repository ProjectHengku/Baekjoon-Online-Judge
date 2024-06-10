using System.Numerics;

class program
{
    static void Main()
    {
        string[] in1 = Console.ReadLine().Split(" ");

        long a = long.Parse(in1[0]); long b = long.Parse(in1[1]);
        long c = (a + b) * (a - b);
        
        Console.WriteLine(c);

    }
}