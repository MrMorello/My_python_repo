using System.Linq;

namespace Myapp1
{
    public class Sorter
    {
        public Sorter()
        {

        }

        public int[] Sort(int[] massive)
        {
            int[] tempMassive;
            if (massive.Length == 1)
            {
                tempMassive = massive;
            }
            else
            {
                int mid_point = massive.Length / 2;
                tempMassive = Merge(Sort(massive.Take(mid_point).ToArray()), Sort(massive.Skip(mid_point).ToArray()));
            }

            return tempMassive;
        }
        public int[] Merge(int[] mass1, int[] mass2)
        {
            int a = 0, b = 0;
            int[] merged = new int[mass1.Length + mass2.Length];
            for (int i = 0; i < mass1.Length + mass2.Length; i++)
            {
                if (b < mass2.Length && a < mass1.Length)
                {
                    if (mass1[a] > mass2[b] && b < mass2.Length)
                    {
                        merged[i] = mass2[b++];
                    }
                    else
                    {
                        merged[i] = mass1[a++];
                    }
                }
                else if (b < mass2.Length)
                {
                    merged[i] = mass2[b++];
                }
                else
                {
                    merged[i] = mass1[a++];
                }
            }
            return merged;
        }
    }
}
