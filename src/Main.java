public class Main {
    public static void main(String[] args) {
        for (int i = 10; i <= 10 & i >= -10; i-- )
            System.out.println("Hello world!" + i);
        {
            System.out.println("**********************");
            for (int a = 1904; a <= 2096; a = a + 4)
                System.out.println("Задание 2" + a);
        }
        {
            System.out.println("**********************");
            for (int i = 7; i <= 98; i = i + 7)
                System.out.println("Последовательность " + i);
        }
        {
            System.out.println("**********************");
            for (int i = 1; i<=512; i = i * 2)
                System.out.println("Умножаем " + i);
        }
        {
            System.out.println("**********************");
            int cont = 29000;
            int sum = 0;
            for (int i = 1; i <= 12; i++) {
                sum = sum + cont;
                System.out.println("Месяц " + i + "," + " сумма накоплений равна " + sum + " рублей");
            }
            {
                System.out.println("**********************");
                int cont1 = 29000;
                int summ = 0;
                for (int i = 1; i <= 12; i++) {
                    summ = summ + ((summ / 100) * 12);
                    summ = summ + cont1;
                    System.out.println("Месяц " + i + "," + " сумма накоплений равна " + summ + " рублей");
                }
            }
        }
    }
}
