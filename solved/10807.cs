class 10807
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string[] strings = Console.ReadLine().Split(" ");
        int v = int.Parse(Console.ReadLine());
        int a = 0;

        for (int i = 0; i < n; i++) {
            if (int.Parse(strings[i]) == v)
            {
                a++;
            }
        }
        Console.WriteLine(a);
    }
}