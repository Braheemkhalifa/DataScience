import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

plt.style.use('ggplot')




try:
      fileName1 = 'Wuzzuf_Job_Posts_Sample.csv'
      df = pd.read_csv(fileName1 , header=0).head(25)
      
      fileName2 = 'Wuzzuf_Applications_Sample.csv'
      df2 = pd.read_csv(fileName2 , header=0).head(25)

except FileNotFoundError:
    print('not found')
    
else:
    
#    df = pd.DataFrame(df)
     pass
    
        
def DrawbarChart(Objects ,Percentage , title , align = "center" , alpha = .5):
    # this is for plotting purpose
       plt.bar(Objects, Percentage, align='center', alpha=0.5)
       plt.xticks(Percentage, Objects )
       plt.title(title)
       plt.show()   


# function to draw piecharr
def DrawpieChart(sizes,labels,title,autopct='%1.1f%%', shadow=True, startangle=140):
        plt.pie(sizes, labels=labels ,autopct=autopct ,shadow=shadow,startangle=startangle)
        plt.title(title)
        plt.legend(loc='upper right', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=2)
        plt.gca().set_aspect("equal")
        plt.show()


#>>> (1) Extract Catgoryrs from csv

     # ---- Category 1
        job_category1 = df.groupby('job_category1').size()
        job_category1_name = job_category1.index
        
        DrawpieChart(job_category1 ,job_category1_name, title ="views")
        DrawbarChart(job_category1_name , job_category1 ,title ="views")
     
     # ---- Category 2
        job_category2 = df.groupby('job_category2').size()
        job_category2_name = job_category2.index
        
        DrawpieChart(job_category2 ,job_category2_name, title ="views")
        DrawbarChart(job_category2_name , job_category2 ,title ="views")

     # ---- Category 3
        job_category3 = df.groupby('job_category3').size()
        job_category3_name = job_category3.index
        
        DrawpieChart(job_category3 ,job_category3_name, title ="views")
        DrawbarChart(job_category3_name , job_category3 ,title ="views")


#>>> (2) Extract job_industry from csv

     # ---- Category 1
        job_industry1 = df.groupby('job_industry1').size()
        job_industry1_name = job_industry1.index
        
        DrawpieChart(job_industry1 ,job_industry1_name, title ="views")
        DrawbarChart(job_industry1_name , job_industry1 ,title ="views")
     
     # ---- Category 2
        job_industry2 = df.groupby('job_industry2').size()
        job_industry2_name = job_industry2.index
        
        DrawpieChart(job_industry2 ,job_industry2_name, title ="views")
        DrawbarChart(job_industry2_name , job_industry2 ,title ="views")

     # ---- Category 2
        job_industry3 = df.groupby('job_industry3').size()
        job_industry3_name = job_industry3.index
        
        DrawpieChart(job_industry3 ,job_industry3_name, title ="views")
        DrawbarChart(job_industry3_name , job_industry3 ,title ="views")


#>>> (3) Extract to draw job id

        job_id_count = df2.groupby('job_id').size()
        job_id_name = job_id_count.index
        
        DrawpieChart(  job_id_count ,job_id_name,title ="views")    
        DrawbarChart(job_id_name , job_id_count ,title ="views")    


#>>> (4) Extract to draw user with jobs 

        user_id_count = df2.groupby('user_id').size()
        user_id_name = user_id_count.index
        
        DrawpieChart(  user_id_count ,user_id_name,title ="views")    
        DrawbarChart(user_id_name , user_id_count ,title ="views")    

#>>> (5) views
        
        Job_id = df["id"]
        Job_Views=df["views"]
        DrawbarChart(Job_id , Job_Views ,title ="views")    
        
        

#>>> (6) Extract to draw user with jobs 

        Select = df.loc[ df['city'] == "Cairo" ]    
        Select

#>>> (7) Show Job Description
        
        Job = "Technical Support Engineer"
        Select_job_data = df.loc[ df['job_name'] ==Job]  
        Select_job_description= Select_job_data["job_description"]
        
        Select_job_description

#>>> (8) Salary  AVG
        
        Select_Job_Salary = df.drop_duplicates(subset="job_title",keep="last")
        
        
        Salary_Max = Select_Job_Salary['salary_maximum']
        Salary_Min = Select_Job_Salary['salary_minimum']
        salary = Salary_Min[Salary_Min < 5000]
        Avg = ( Salary_Max + Salary_Min ) / 2
        Select_Job_Id = Select_Job_Salary["id"]
        
        
        DrawbarChart(Select_Job_Id , Avg ,title ="views")    
        DrawpieChart( Avg ,Select_Job_Id ,title ="views")    


