string[] strings = Console.ReadLine().Split(" ");
double check = 0;

for (int i = 0; i < strings.Length; i++)
{
    check = check + Math.Pow(double.Parse(strings[i]), 2);
}

check = check%10 ;
Console.WriteLine(check);