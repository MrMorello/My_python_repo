using System;

namespace Myapp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите чисело элементов последовательности");
            string elementCount = Console.ReadLine();

            int elem_nums;
            while (!Int32.TryParse(elementCount, out elem_nums))
            {
                Console.WriteLine("Введите чисело элементов последовательности");
                elementCount = Console.ReadLine();
            }

            int[] mas = new int[elem_nums];
            Console.WriteLine($"Введите {elem_nums} натуральных чисел. Здесь надо посмотреть Int32.Max ");
            //здесь нужна проверка что число натуральное, что оно больше нуля и что оно меньше Int32.Max 

            for (int i = 0; i < mas.Length; i++)
            {
                Console.Write("{0}-е число: ", i + 1);
                string elementString = Console.ReadLine();
                int element;
                while(!Int32.TryParse(elementString, out element))
                {
                    Console.WriteLine("Введите число. {0}-е число: ", i + 1);
                    elementString = Console.ReadLine();
                }

                mas[i] = element; 
            }

            Sorter sorter = new Sorter();

            Console.WriteLine(string.Join(",", sorter.Sort(mas)));
            Console.ReadKey();

        }

    }
}