import os
import csv

# specify the csv file path
File_to_Load = os.path.join("Resources/budget_data.csv")
print(File_to_Load)

File_to_Output = os.path.join("Analysis/Txt_File")

#Setting up variables
Total_Months = 0 #starts at zero and will increase as it loops thru data
Prev_Revenue = 0 #will use to calculate the revenue change for each month
Month_of_Change = [] #currently empty and will append later
Revenue_Change_List = []
Revenue_Change = 0
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 0]
Total_Revenue = 0 #starts at zero and will increase as it loops thru data

#read the csv file and then convert it to a list of dictonary
with open(File_to_Load) as Revenue_Data:
    reader = csv.DictReader(Revenue_Data)

    #loop through each row in data set
    for row in reader:

        #Track the totals
        Total_Months = Total_Months + 1 #will loop thru and count each row
        Total_Revenue = Total_Revenue + int(row["Profit/Losses"]) #will loop thru each row and add the values 

        #track the revenue change
        Revenue_Change = int(row["Profit/Losses"]) - Revenue_Change
        Prev_Revenue = int(row["Profit/Losses"])
        Revenue_Change_List = Revenue_Change_List + [Revenue_Change]
        Month_of_Change.append(row["Date"])

        #Calculate the greatest increase
        if (Revenue_Change > Greatest_Increase[1]):
            Greatest_Increase[0] = row["Date"]
            Greatest_Increase[1] = Revenue_Change

        #Calculate the greatest decrease
        if (Revenue_Change > Greatest_Decrease[1]):
            Greatest_Decrease[0] = row["Date"]
            Greatest_Decrease[1] = Revenue_Change

#calculate the average revenue change
Revenue_Avg = sum(Revenue_Change_List) / len(Revenue_Change_List)

output = (
     f"\nFinancial Analysis\n"
     f"----------------------------\n"
     f"Total Months: {Total_Months}\n"
     f"Total: ${Total_Revenue}\n"
     f"Average Revenue Change: ${Revenue_Avg:.2f}\n"
     f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
     f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n"
 )

#print the output
print(output)

#export the results to the text file
with open(File_to_Output, "w") as Txt_File:
    Txt_File.write(output)







