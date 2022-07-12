#import os and csv Modules
import os 
import csv


# Set path for the budget_data file located in Resources folder
csv_path = os.path.join('Resources', "election_data.csv")

# function to analyze the csv file
def election_data_analysis(csv_path):
    with open(csv_path) as file:
        csv_reader=csv.reader(file,delimiter=",")
       
        # Read the header row
        csv_header = next(csv_reader)
        candidates_list=[]
        candidates_poll=[]
        
        # loop through all the rows
        for row in csv_reader:
            candidates_poll.append(row[2])
            if not row[2] in candidates_list:
                candidates_list.append(row[2])
        
        
    Total_Votes= len(candidates_poll)      
    candidates_percent=[candidates_poll.count(candidate)/Total_Votes for candidate in candidates_list ]     
    candidates_count=[candidates_poll.count(candidate) for candidate in candidates_list ]     
    winner = list({k: v for k, v in zip(candidates_list, candidates_count) if v==max(candidates_count)}.keys())[0]
    return candidates_list,Total_Votes,candidates_percent,candidates_count,winner


# Set function to write the election result in the text file
def text_writer(csv_input,txt_Election_Results):
    # Set path for files
    input_path=os.path.join("Resources",csv_input)
    output_path = os.path.join("analysis", txt_Election_Results)
    candidates_list,Total_Votes,candidates_percent,candidates_count,winner=election_data_analysis(input_path)
    
    # Write in the text file located in analysis foler
    f= open(output_path,"w+")
    f.write("Election Results\n")
    f.write("---------------------------"+"\n")
    f.write(f"Total Votes: {Total_Votes}\n")
    f.write("---------------------------"+"\n")
    for i in range(len(candidates_list)):
        f.write(("{}" + ": "+ "{:.3%} " +"("+"{}"+")").format(candidates_list[i],candidates_percent[i],candidates_count[i]))
        f.write("\n")
    f.write("---------------------------"+"\n")
    f.write(f"Winner: {winner}\n")
    f.write("---------------------------"+"\n")
    f.close()

    # Print the final results in Terminal
    print("---------------------------")
    print("Election Results\n")
    print("---------------------------")
    print(f"Total Votes:{Total_Votes}\n")
    print("---------------------------")
    for i in range(len(candidates_list)):
        print(("{}" + ": "+ "{:.3%} " +"("+"{}"+")").format(candidates_list[i],candidates_percent[i],candidates_count[i]))
        print("\n")
    print("---------------------------")
    print(f"Winner: {winner}\n")
    print("---------------------------")
   

text_writer("election_data.csv","Election_Results.txt")