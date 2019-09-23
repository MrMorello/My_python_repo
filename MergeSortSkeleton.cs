using System;
using System.Linq;

namespace Myapp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] mas = new int[] { 1, 3, 4, 5, 6, 6, 8, 2, 5, 9, 0 };
            Console.WriteLine(string.Join(",", Sort(mas)));
            Console.ReadKey();

        }
        public static int[] Sort(int[] massive)
        {
            if (massive.Length == 1)
                return massive;
            int mid_point = massive.Length / 2;
            return Merge(Sort(massive.Take(mid_point).ToArray()), Sort(massive.Skip(mid_point).ToArray()));
        }
        public static int[] Merge(int[] mass1, int[] mass2)
        {
            int a = 0, b = 0;
            int[] merged = new int[mass1.Length + mass2.Length];
            for (int i = 0; i < mass1.Length + mass2.Length; i++)
            {
                if (b < mass2.Length && a < mass1.Length)
                    if (mass1[a] > mass2[b] && b < mass2.Length)
                        merged[i] = mass2[b++];
                    else
                        merged[i] = mass1[a++];
                else
                    if (b < mass2.Length)
                    merged[i] = mass2[b++];
                else
                    merged[i] = mass1[a++];
            }
            return merged;
        }
    }
}
