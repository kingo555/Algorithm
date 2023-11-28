import java.util.Scanner;

public class Main
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		
		for (int i=0; i<N; i++)
		{
			String S=sc.next();
			String first=String.valueOf(S.charAt(0));
			String last=String.valueOf(S.charAt(S.length()-1));
			
			System.out.println(first+last);
		}
		sc.close();

	}
}