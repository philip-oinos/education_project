import pandas as pd
from  matplotlib import pyplot as plt

#reading in .csv file
timesdata = pd.read_csv('C:Users/theoi/Desktop/Data_Project/Education_Data/timesData.csv', delimiter=",")

#selecting certain columns out of .csv file
students_scores_dataframe = timesdata[['university_name','num_students','total_score','teaching','international']]

#removing values from number of students column that are less than 0
filtered_students_score_df = students_scores_dataframe[students_scores_dataframe['num_students'] > 0]
#removing values from total score column that are less than 0
filtered_students_score_df = students_scores_dataframe[students_scores_dataframe['total_score'] >= 0]
#print(filtered_students_score_df)



#setting up scatter plott
x = filtered_students_score_df['total_score']
y = filtered_students_score_df['num_students'] 
sizes = filtered_students_score_df['international']

#building scatter plot
plt.style.use('seaborn-bright')
plt.scatter(x,y,s=75, cmap='Greens', edgecolor='black', linewidth=1, alpha=0.60)
cbar = plt.colorbar()
cbar.set_label('Teaching')
plt.title('World Education Stats: Number of Students & Total Score')
plt.xlabel('Total Score')
plt.ylabel('Number of Students')

#showing scatter plot
plt.show()