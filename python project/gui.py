# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

fileName1 = 'Wuzzuf_Job_Posts_Sample.csv'
df = pd.read_csv(fileName1 , header=0).head(25)
      
fileName2 = 'Wuzzuf_Applications_Sample.csv'
df2 = pd.read_csv(fileName2 , header=0).head(25)

class Ui_Form(object):
    def setupUi(self, Form):


        Form.setObjectName("Form")
        Form.resize(812, 592)
        Form.setMaximumSize(QtCore.QSize(812, 592))
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 0, 127);\n"
"\n"
"}")
        self.JobDescription_2 = QtWidgets.QGroupBox(Form)
        self.JobDescription_2.setGeometry(QtCore.QRect(190, 20, 601, 80))
        self.JobDescription_2.setStyleSheet("QGroupBox{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.JobDescription_2.setObjectName("JobDescription_2")
        self.Jobsearch = QtWidgets.QLineEdit(self.JobDescription_2)
        self.Jobsearch.setGeometry(QtCore.QRect(100, 30, 301, 31))
        self.Jobsearch.setStyleSheet("QLineEdit{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.Jobsearch.setObjectName("Jobsearch")
        self.JobsearchBtn = QtWidgets.QPushButton(self.JobDescription_2)
        self.JobsearchBtn.setGeometry(QtCore.QRect(420, 30, 81, 31))
        self.JobsearchBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.JobsearchBtn.setObjectName("JobsearchBtn")
        self.JobsearchBtn.clicked.connect(self.Get_JoB_Description)
        # 7) Show Job Description
        self.Details = QtWidgets.QGroupBox(Form)
        self.Details.setGeometry(QtCore.QRect(190, 110, 601, 462))
        self.Details.setStyleSheet("QGroupBox{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.Details.setObjectName("Details")
        self.ChooseSearch = QtWidgets.QComboBox(self.Details)
        self.ChooseSearch.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.ChooseSearch.setStyleSheet("QComboBox{\n"
"\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"  \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.ChooseSearch.setObjectName("ChooseSearch")
        self.ChooseSearch.addItem("")
        self.ChooseSearch.addItem("")
        self.ChooseSearch.addItem("")
        self.ChooseSearch.addItem("")
        self.InputSearch = QtWidgets.QLineEdit(self.Details)
        self.InputSearch.setGeometry(QtCore.QRect(150, 30, 351, 31))
        self.InputSearch.setStyleSheet("QLineEdit{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.InputSearch.setObjectName("InputSearch")
        self.SearchBtn = QtWidgets.QPushButton(self.Details)
        self.SearchBtn.setGeometry(QtCore.QRect(510, 30, 81, 31))
        self.SearchBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.SearchBtn.setObjectName("SearchBtn")
        self.SearchBtn.clicked.connect(self.Search_In_Case) 
       #(8) Extract to draw user with jobs 
        self.textBrowser = QtWidgets.QTextBrowser(self.Details)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 581, 372))
        self.textBrowser.setStyleSheet("QTextBrowser\n"
"{\n"
" \n"
"    width: min-content;\n"
"      white-space: nowrap;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.textBrowser.setObjectName("textBrowser")
        self.Visualize = QtWidgets.QGroupBox(Form)
        self.Visualize.setGeometry(QtCore.QRect(20, 20, 161, 551))
        self.Visualize.setStyleSheet("QGroupBox{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.Visualize.setObjectName("Visualize")
        self.SelectChart = QtWidgets.QComboBox(self.Visualize)
        self.SelectChart.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.SelectChart.setStyleSheet("QComboBox{\n"
"\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"  \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.SelectChart.setObjectName("SelectChart")
        self.SelectChart.addItem("")
        self.SelectChart.addItem("")


        self.SelectCategory = QtWidgets.QComboBox(self.Visualize)
        self.SelectCategory.setGeometry(QtCore.QRect(20, 150, 121, 31))
        self.SelectCategory.setStyleSheet("QComboBox{\n"
"\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"  \n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.SelectCategory.setObjectName("SelectCategory")
        self.SelectCategory.addItem("")
        self.SelectCategory.addItem("")
        self.SelectCategory.addItem("")
        self.SelectCategory.addItem("")
        self.SelectCategory.addItem("")
        self.SelectCategory.addItem("")
        self.Showbtn = QtWidgets.QPushButton(self.Visualize)
        self.Showbtn.setGeometry(QtCore.QRect(20, 190, 121, 31))
        self.Showbtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    font: 17pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.Showbtn.setObjectName("Showbtn")
        self.Showbtn.clicked.connect(self.Show_Plot)
        # 1),2) Show Methods (Category and Industry)
        
        self.JobViewsBtn = QtWidgets.QPushButton(self.Visualize)
        self.JobViewsBtn.setGeometry(QtCore.QRect(20, 230, 121, 31))
        self.JobViewsBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.JobViewsBtn.setObjectName("JobViewsBtn")
        self.JobViewsBtn.clicked.connect(self.Show_Jobs_views)
        # 5) views
        self.JobApplicantBtn = QtWidgets.QPushButton(self.Visualize)
        self.JobApplicantBtn.setGeometry(QtCore.QRect(20, 270, 121, 31))
        self.JobApplicantBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.JobApplicantBtn.setObjectName("JobApplicantBtn")
        self.JobApplicantBtn.clicked.connect(self.Show_Job_statistics)
        # 3) Extract to draw job id
        self.SalaryAverageBtn = QtWidgets.QPushButton(self.Visualize)
        self.SalaryAverageBtn.setGeometry(QtCore.QRect(20, 310, 121, 31))
        self.SalaryAverageBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.SalaryAverageBtn.setObjectName("SalaryAverageBtn")
        self.SalaryAverageBtn.clicked.connect(self.Show_Salary_Avg)
        # 6) Salary  AVG
        self.UserApplicantBtn = QtWidgets.QPushButton(self.Visualize)
        self.UserApplicantBtn.setGeometry(QtCore.QRect(20, 350, 121, 31))
        self.UserApplicantBtn.setStyleSheet("QPushButton\n"
"{\n"
"      \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}")
        self.UserApplicantBtn.setObjectName("UserApplicantBtn")
        self.UserApplicantBtn.clicked.connect(self.Show_User_statistics_With_Jobs)
        # 4) Extract to draw user with jobs
        self.label = QtWidgets.QLabel(self.Visualize)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"  \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        self.JobDescription_2.setTitle(_translate("Form", "Job Description"))
        self.JobsearchBtn.setText(_translate("Form", "Search"))
        
        self.Details.setTitle(_translate("Form", "Records Details"))
        self.ChooseSearch.setItemText(0, _translate("Form", "City"))
        self.ChooseSearch.setItemText(1, _translate("Form", "Job"))
        self.ChooseSearch.setItemText(2, _translate("Form", "Category"))
        self.ChooseSearch.setItemText(3, _translate("Form", "Industry"))
        self.SearchBtn.setText(_translate("Form", "Search"))
        
        self.Visualize.setTitle(_translate("Form", "Visualize"))
        self.SelectChart.setItemText(0, _translate("Form", "Bar Chart"))
        self.SelectChart.setItemText(1, _translate("Form", "Pie Chart"))
        self.SelectCategory.setItemText(0, _translate("Form", "Category 1"))
        self.SelectCategory.setItemText(1, _translate("Form", "Category 2"))
        self.SelectCategory.setItemText(2, _translate("Form", "Category 3"))
        self.SelectCategory.setItemText(3, _translate("Form", "Industry 1"))
        self.SelectCategory.setItemText(4, _translate("Form", "industry 2"))
        self.SelectCategory.setItemText(5, _translate("Form", "industry 3"))
        self.Showbtn.setText(_translate("Form", "Show"))
        self.JobViewsBtn.setText(_translate("Form", "Job Views"))
        self.JobApplicantBtn.setText(_translate("Form", "Jobs Applicant"))
        self.SalaryAverageBtn.setText(_translate("Form", "Salary Average"))
        self.UserApplicantBtn.setText(_translate("Form", "Users Applicant"))
        self.label.setText(_translate("Form", "Chart Type :"))
    
    def DrawpieChart(self,labels,sizes,title,autopct='%1.1f%%', shadow=True, startangle=140):
        
            plt.pie(sizes, labels=labels ,autopct=autopct ,shadow=shadow,startangle=startangle)
            plt.title(title)
            plt.legend(loc='upper right', bbox_to_anchor=(0.5, -0.05),  shadow=True, ncol=2)
            plt.gca().set_aspect("equal")
            plt.show()

    def DrawbarChart(self,Objects ,Percentage , title , align = "center" , alpha = .5):
           plt.bar(Objects, Percentage, align='center', alpha=0.5,color='r')
           plt.xticks(Percentage, Objects )
           plt.title(title)
           plt.show()   


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 1),2) Show Methods (Category and Industry)
   
    def Show_Plot(self):
        
        
    #>>>>>>>>>>>>> Bar Chart 
        
        if self.SelectChart.currentText() == 'Bar Chart': 
    
         #>>>>>>>>>>>>> Category (1) 
            if self.SelectCategory.currentText() == 'Category 1' :
               job_category1 = df.groupby('job_category1').size()
               job_category1_name = job_category1.index 
               
               self.DrawbarChart(job_category1_name , job_category1 ,title ="Category 1")
       
        #>>>>>>>>>>>>> Category (2) 
            if self.SelectCategory.currentText() == 'Category 2' :
               job_category2 = df.groupby('job_category2').size()
               job_category2_name = job_category2.index
               
               self.DrawbarChart(job_category2_name , job_category2 ,title ="Category 2")
       
        #>>>>>>>>>>>>> Category (3) 
            if self.SelectCategory.currentText() == 'Category 3' :
               job_category3 = df.groupby('job_category3').size()
               job_category3_name = job_category1.index 
        
               self.DrawbarChart(job_category3_name , job_category3 ,title ="Category 3")
         
        #>>>>>>>>>>>>> Industry (1) 
            if self.SelectCategory.currentText() == 'Industry 1' :
               job_industry1 = df.groupby('job_industry1').size()
               job_industry1_name = job_industry1.index
        
               self.DrawbarChart(job_industry1_name , job_industry1 ,title ="Industry 1")
        
       #>>>>>>>>>>>>> Industry (2) 
            if self.SelectCategory.currentText() == 'Industry 2' :
               job_industry2 = df.groupby('job_industry2').size()
               job_industry2_name = job_industry2.index
               
               self.DrawbarChart(job_industry2_name , job_industry2 ,title ="Industry 2")
        
        #>>>>>>>>>>>>> Industry (3) 
            if self.SelectCategory.currentText() == 'Industry 3' :
               job_industry3 = df.groupby('job_industry3').size()
               job_industry3_name = job_industry3.index 
        
               self.DrawbarChart(job_industry3_name , job_industry3 ,title ="Industry 3")


    #>>>>>>>>>>>>> pie Chart 

        if self.SelectChart.currentText() == 'Pie Chart': 
         #>>>>>>>>>>>>> Category (1) 
            if self.SelectCategory.currentText() == 'Category 1' :
               job_category1 = df.groupby('job_category1').size()
               job_category1_name = job_category1.index 
               
               self.DrawpieChart(job_category1_name , job_category1 ,title ="Category 1")
       
        #>>>>>>>>>>>>> Category (2) 
            if self.SelectCategory.currentText() == 'Category 2' :
               job_category2 = df.groupby('job_category2').size()
               job_category2_name = job_category2.index
               
               self.DrawpieChart(job_category2_name , job_category2 ,title ="Category 2")
       
        #>>>>>>>>>>>>> Category (3) 
            if self.SelectCategory.currentText() == 'Category 3' :
               job_category3 = df.groupby('job_category3').size()
               job_category3_name = job_category1.index 
        
               self.DrawpieChart(job_category3_name , job_category3 ,title ="Category 3")
         
         #>>>>>>>>>>>>> Industry (1) 
            if self.SelectCategory.currentText() == 'Industry 1' :
               job_industry1 = df.groupby('job_industry1').size()
               job_industry1_name = job_industry1.index
        
               self.DrawpieChart(job_industry1_name , job_industry1 ,title ="Industry 1")
        
        #>>>>>>>>>>>>> Industry (2) 
            if self.SelectCategory.currentText() == 'Industry 2' :
               job_industry2 = df.groupby('job_industry2').size()
               job_industry2_name = job_industry2.index
               
               self.DrawpieChart(job_industry2_name , job_industry2 ,title ="Industry 2")
        
        #>>>>>>>>>>>>> Industry (3) 
            if self.SelectCategory.currentText() == 'Industry 3' :
               job_industry3 = df.groupby('job_industry3').size()
               job_industry3_name = job_industry3.index 
        
               self.DrawpieChart(job_industry3_name , job_industry3 ,title ="Industry 3")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3) Extract to draw job id
               
    def Show_Job_statistics (self):
        
         job_id_count = df2.groupby('job_id').size()
         job_id_name = job_id_count.index
        #>>>>>>>>>>>>> Bar Chart   
         if self.SelectChart.currentText() == 'Bar Chart': 
            self.DrawbarChart(job_id_name , job_id_count ,title ="Job id")            
       #>>>>>>>>>>>>> Bar Chart        
         if self.SelectChart.currentText() == 'Pie Chart': 
            self.DrawpieChart(  job_id_count ,job_id_name,title ="Job id")    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 4) Extract to draw user with jobs
               
    def Show_User_statistics_With_Jobs (self):
        
        user_id_count = df2.groupby('user_id').size()
        user_id_name = user_id_count.index 
        #>>>>>>>>>>>>> Bar Chart   
        if self.SelectChart.currentText() == 'Bar Chart': 
            self.DrawbarChart(user_id_name , user_id_count ,title ="Show_User_statistics_With_Jobs")    

       #>>>>>>>>>>>>> Bar Chart        
        if self.SelectChart.currentText() == 'Pie Chart': 
            self.DrawpieChart( user_id_count ,user_id_name,title ="Show_User_statistics_With_Jobs")    
                      
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 5) views
               
    def Show_Jobs_views (self):
        
        Job_id = df["id"]
        Job_Views=df["views"]
        self.DrawbarChart(Job_id , Job_Views ,title ="Jobs Views")                          

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 6) Salary  AVG
               
    def Show_Salary_Avg (self):
        
        Select_Job_Salary = df.drop_duplicates(subset="job_title",keep="last")
        Salary_Max = Select_Job_Salary['salary_maximum']
        Salary_Min = Select_Job_Salary['salary_minimum']        
        Avg = ( Salary_Max + Salary_Min ) / 2
        Select_Job_Id = Select_Job_Salary["id"]
        #>>>>>>>>>>>>> Bar Chart   
        if self.SelectChart.currentText() == 'Bar Chart': 
            self. DrawbarChart(Select_Job_Id , Avg ,title ="Salary Avg")    
            #>>>>>>>>>>>>> Bar Chart        
        if self.SelectChart.currentText() == 'Pie Chart': 
            self.DrawbarChart(Select_Job_Id , Avg ,title ="Salary Avg")    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 7) Show Job Description

    def Get_JoB_Description (self):      
        Job = self.Jobsearch.text()
        Select_job_data = df.loc[ df['job_title'] ==Job]    
        Select_job_description = Select_job_data.iat[0,16]
        self.textBrowser.setText(str(Select_job_description))        
       
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (8) Extract to draw user with jobs 
    def Search_In_Case (self):
       
         #>>>>>>>>>>>>> City 
             if self.ChooseSearch.currentText() == 'City' :
                City = self.InputSearch.text()
                Select = df.loc[ df['city'] == City ]    
                self.textBrowser.setText(str(Select))        
                
         #>>>>>>>>>>>>> Job Title
             if self.ChooseSearch.currentText() == 'Job' :
                Job = self.InputSearch.text()
                Select = df.loc[ df['job_title'] == Job ]    
                self.textBrowser.setText(str(Select))        

         #>>>>>>>>>>>>> Category 
             if self.ChooseSearch.currentText() == 'Category' :
                Category = self.InputSearch.text()
                Select = df.loc[ df['job_category2'] == Category ]    
                self.textBrowser.setText(str(Select))        

         #>>>>>>>>>>>>> Industry 
             if self.ChooseSearch.currentText() == 'Industry' :
                Industry = self.InputSearch.text()
                Select = df.loc[ df['job_industry3'] == Industry ]    
                self.textBrowser.setText(str(Select))        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

