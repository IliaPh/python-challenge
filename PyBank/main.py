#import os and csv modules
import os 
import csv

# Set path for the budget_data.csv file located in Resources folder:
csv_path = os.path.join('Resources', "budget_data.csv")

# Set function to analyze csv file
def budget_data_analysis(csv_path):
    with open(csv_path) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=",")
        
        # Read the header row
        csv_header = next(csv_reader)
        profit_loss=[]
        Date=[]
        
        # loop through all the rows
        for row in csv_reader:
            profit_loss.append(row[1])
            Date.append(row[0])
    Total_Months=len(Date)

    profit_loss=[int(i) for i in profit_loss]
    Total=sum(profit_loss)

    Changes=[profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
    Average_Change= sum(Changes)/len(Changes)
    Greatest_Increase_amount= max(Changes)
    Greatest_Increase_Date= Date[Changes.index(max(Changes))+1]
    Greatest_Decrease_amount= min(Changes)
    Greatest_Decrease_date= Date[Changes.index(min(Changes))+1]
    return Total_Months,Total,Average_Change,Greatest_Increase_amount,\
         Greatest_Increase_Date,Greatest_Decrease_amount,Greatest_Decrease_date   


# Set function to write the analysis result in text file
def text_writer(csv_input,txt_Final_Results):
    
    # Set path for files
    input_path=os.path.join('', "Resources",csv_input)
    Final_Results_path = os.path.join('', "Analysis", txt_Final_Results)
    Total_Months,Total,Average_Change,Greatest_Increase_amount,\
    Greatest_Increase_Date,Greatest_Decrease_amount,Greatest_Decrease_date=\
    budget_data_analysis(input_path)
    
    # Write in text Final_Results file
    f= open(Final_Results_path,"w+")
    f.write("Financial Analysis\n")
    f.write("-------------------------------"+"\n")
    f.write(f"Total Months: {Total_Months}\n")
    f.write(f"Total: ${Total}\n")
    f.write(f"Average  Change: ${round(Average_Change,2)}\n")
    f.write(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_amount})\n")
    f.write(f"Greatest Decrease in Profits: {Greatest_Decrease_date} (${Greatest_Decrease_amount})\n")
    f.write("-------------------------------"+"\n")
    f.close()

    # Print the final results in terminal
    print("-------------------------------"+"\n")
    print("Financial Analysis\n")
    print("-------------------------------"+"\n")
    print(f"Total Months: {Total_Months}\n")
    print(f"Total: ${Total}\n")
    print(f"Average  Change: ${round(Average_Change,2)}\n")
    print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_amount})\n")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_date} (${Greatest_Decrease_amount})\n")


text_writer("budget_data.csv","Final_Results.txt")