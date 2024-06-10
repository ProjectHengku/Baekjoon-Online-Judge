string gr = Console.ReadLine();
float sc = 0;

if (gr == "A+")
{
    sc = 4.3f;
}
else if (gr == "A0")
{
    sc = 4.0f;
}
else if (gr == "A-")
{
    sc = 3.7f;
}
else if (gr == "B+")
{
    sc = 3.3f;
}
else if (gr == "B0")
{
    sc = 3.0f;
}
else if (gr == "B-")
{
    sc = 2.7f;
}
else if (gr == "C+")
{
    sc = 2.3f;
}
else if (gr == "C0")
{
    sc = 2.0f;
}
else if (gr == "C-")
{
    sc = 1.7f;
}
else if (gr == "D+")
{
    sc = 1.3f;
}
else if (gr == "D0")
{
    sc = 1.0f;
}
else if (gr == "D-")
{
    sc = 0.7f;
}
else if (gr == "F")
{
    sc = 0.0f;
}
Console.WriteLine(string.Format("{0:0.0}", sc));