using System.Numerics;

class program
{
    static void Main()
    {
        string[] in1 = Console.ReadLine().Split(" ");

        int x = int.Parse(in1[0]); int y = int.Parse(in1[1]);
        int[,] matA = new int[x, y];
        int[,] matB = new int[x, y];

        int[,] matC = new int[x, y];
        string answer = null;

        for (int i = 0; i < x; i++)
        {
            string[] inputA = Console.ReadLine().Split(" ");
            for (int j = 0; j < y; j++)
            {
                matA[i, j] = int.Parse(inputA[j]);
            }
        }

        for (int i = 0; i < x; i++)
        {
            string[] inputB = Console.ReadLine().Split(" ");
            for (int j = 0; j < y; j++)
            {
                matB[i, j] = int.Parse(inputB[j]);
            }
        }

        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                matC[i, j] = matA[i, j] + matB[i, j];
            }
            for (int k = 0; k < y-1; k++)
            {
                answer = answer + matC[i, k] + " ";
            }
            answer = answer + matC[i, y-1];

            Console.WriteLine(answer);
            answer = null;
        }
    }
}