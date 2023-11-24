//gmail_signup_project_vjsharanv.c

#include<stdio.h>
union gmail_signup
{
	char fname[10];
	char lname[10];
	int age;
	char gender[6];
	char dob[12];
	char lang[10];	
		union security
		{
			char username[15];
			char password[12];
			char conf[12];
			char num[10];
			long pin;
			char country[10];
		}s;
}g[3];
void main()
{
	int accounts,i;
	FILE *ids;
	ids=fopen("G-Mail Accountzz.txt","a");
	//code by vijaysharanv
	repeatu:
	printf("Enter the number of accounts (Maxx=3): ");
	scanf("%d",&accounts);
	if (accounts>3)
	{
		printf("\nOnly 3 or lesser accounts can be created. Please try again...");
		printf("\n=============Try Again=============");
		goto repeatu;
	}
	else
	{
		for (i=0;i<accounts;i++);
		{
			printf("Enter your firstname: ");
			scanf("%s",g[i].fname);
			fprintf(ids,"\nFirst Name : %s",g[i].fname);
			
			printf("Enter your lastname: ");
			scanf("%s",g[i].lname);
			fprintf(ids,"\nLast Name : %s",g[i].lname);
			//code by vijaysharanv
			printf("Enter your age: ");
			scanf("%d",&g[i].age);
			fprintf(ids,"\nAge : %d",g[i].age);
			
			printf("Enter your gender: ");
			scanf("%s",g[i].gender);
			fprintf(ids,"\nGender: %s",g[i].gender);
			
			printf("Enter your Date of Birth [In DD-MM-YYYY Format]: ");
			scanf("%s",g[i].dob);
			fprintf(ids,"\nDOB: %s",g[i].dob);
			
			printf("In what language do you want to use Google: ");
			scanf("%s",g[i].lang);
			fprintf(ids,"\nPrimary Language: %s",g[i].lang);
			
			printf("Enter your username: ");
			scanf("%s",g[i].s.username);//code by vijaysharanv
			fprintf(ids,"\nUsername: %s",g[i].s.username);
			
			printf("Enter your password: ");
			scanf("%s",g[i].s.password);
			fprintf(ids,"\nPassword: %s",g[i].s.password);
			
			printf("Confirm your password: ");
			scanf("%s",g[i].s.conf);
			fprintf(ids,"\nPassword Confirmation: %s",g[i].s.conf);
			
			printf("Enter your number: ");
			scanf("%s",g[i].s.num);
			fprintf(ids,"\nPhone Number: %s",g[i].s.num);
			
			printf("Enter your pincode: ");
			scanf("%ld",g[i].s.password);
			fprintf(ids,"\n Pincode: %ld",g[i].s.pin);
			
			printf("Enter your country: ");
			scanf("%s",g[i].s.country);
			fprintf(ids,"\n Country: %s",g[i].s.country);
			
			fprintf(ids,"\n\n=======================x=x=x=======================");
		}
	
	}//code by vijaysharanv
	fclose(ids);	
}
