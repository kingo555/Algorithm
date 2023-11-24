import java.util.Scanner;

public class Main
{
	public static void main(String args[])
	{
		Scanner sc= new Scanner(System.in);
		int N=sc.nextInt();
		int arr[]=new int[N];
		double arr1[]=new double[N];
		int max=0;
		double sum=0;
		double avg=0;
		
		for (int i=0; i<N; i++)
		{
			arr[i]=sc.nextInt();
			if (max<arr[i]) max=arr[i];
		}
		
		for (int i=0; i<N; i++)
		{
			arr1[i]=(double)arr[i]*100/max;
			sum+=arr1[i];
		}
		
		avg=sum/N;
		System.out.println(avg);

	}

}