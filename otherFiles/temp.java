import java.util.*;
import java.io.*;
class temp
{
	public static void main(String args[])throws Exception
	{
		File file = new File("D:\\dip\\NASDAQ.txt");
		BufferedReader br = new BufferedReader(new FileReader(file)); 
		String str;
 	 while ((str = br.readLine()) != null) {
   	 StringTokenizer st=new StringTokenizer(str,",");
		while(st.hasMoreTokens())
		{
		System.out.print(st.nextToken()+"\n");
		st.nextToken();
		}
	}
} 
		
	
}