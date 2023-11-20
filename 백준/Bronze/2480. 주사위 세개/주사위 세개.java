import java.util.Scanner;

public class Main
{
	public static void main(String args[])
	{
		int a,b,c,money;
		
		Scanner sc=new Scanner(System.in);
		a=sc.nextInt();
		b=sc.nextInt();
		c=sc.nextInt();
		
		if (a==b&&b==c) { money=10000+a*1000;}
		else if (a==b&&a!=c&&c!=b) {money=1000+a*100;}
		else if (b==c&&b!=a&&c!=a) {money=1000+b*100;}
		else if (a==c&&a!=b&&c!=b) {money=1000+c*100;}
		else { 
			int max=a;
			if (a<b&&b>c) {max=b;}
			else if (a<c&&b<c) {max=c;}
			money=max*100;
		}
		System.out.println(money);
	}
}