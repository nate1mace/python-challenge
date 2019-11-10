
# Store the file path associated with the file (note the backslash may be OS specific)
import os
import csv
import subprocess

csvpath = os.path.join('Instructions','PyBank','Resources','budget_data.csv')

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile)

    #Set Variables to zero, create open arrays
    totpl = 0
    maxprofit = 0
    minprofit = 0
    #diffprof = []
    revenue = []
    #Skip header row
    csv_header = next(csvreader)

    #Define function
    def finAnyl(tmonths,totpl,avchange,gimonth,maxprofit,gdmonth,minprofit):
        print("----------------------------------------------------")
        print("Financial Analysis")
        print("----------------------------------------------------")
        print("Total Months: " + str(tmonths))
        print("Total: $" + str(totpl))
        print("Average Change: $" + str(round(avchange,2)))
        print("Greatest Increase in Profits: " + gimonth + " ($" + str(maxprofit) + ")")
        print("Greatest Decrease in Profits: " + gdmonth + " ($" + str(minprofit) + ")")
        print("----------------------------------------------------")
        
    #take list of csv to find length
    data = list(csvreader)
    for row in data:
        #length of data indicates total months
        tmonths = len(data)
        #total profit loss is summed for each row
        totpl = int(row[1]) + totpl
        #create a revenue array
        revenue.append(float(row[1]))
        diffprof = []
        #run thru all revenues, subtract one from length because we are taking the difference between row i and row i+1
        for i in range (0,len(revenue) - 1):
            diffprof.append(revenue[i+1] - revenue[i])
            #if the profit difference is greater than the current max increase in profit, the value is overwritten with the greater value
            #the month for the row of the greatest difference is taken
            if maxprofit < diffprof[i]:
                maxprofit = diffprof[i]
                gimonth = (row[0])
            if minprofit > diffprof[i]:
                minprofit = diffprof[i]    
                gdmonth = (row[0])
    avchange = sum(diffprof)/tmonths    

    #Print function
    print(finAnyl(tmonths,totpl,avchange,gimonth,maxprofit,gdmonth,minprofit))

    #output text file
    with open("bank_results.txt","w") as txt_file:
        txt_file.write("----------------------------------------------------" + '\n' +
        "Financial Analysis" + '\n' +
        "----------------------------------------------------" + '\n' +
        "Total Months: " + str(tmonths) + '\n' +
        "Total: $" + str(totpl) + '\n' +
        "Average Change: $" + str(round(avchange,2)) + '\n' +
        "Greatest Increase in Profits: " + gimonth + " ($" + str(maxprofit) + ")" + '\n' +
        "Greatest Decrease in Profits: " + gdmonth + " ($" + str(minprofit) + ")" + '\n' +
        "----------------------------------------------------")
        
    