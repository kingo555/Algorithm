import java.util.*;

public class Main
{
	public static void main(String args[])
	{
		Scanner sc= new Scanner(System.in);
		
		HashSet<Integer> s= new HashSet<>();
		for (int i=0; i<10; i++)
		{
			int a= sc.nextInt();
			s.add(a%42);
		}
		System.out.println(s.size());
	}
}

