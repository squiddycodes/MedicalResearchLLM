import csv
fileName = r"\20k_abstracts\train.txt"#txt file containing the 
with open(fileName, "r") as file:
    x = {}
    curr = "###24293578"#first PMID
    for line in file:
        if line != "\n":
            if line.split()[0] == "METHODS":
                line = line.replace("METHODS","")
                line = line.replace("\n","")
                line = line.replace("  ","") 
                line = line.replace("\t","")
                x[curr] += line #append to methodology line
            elif line.split()[0] == "OBJECTIVE":
                line = line.replace("OBJECTIVE","")
                line = line.replace("\n","")
                line = line.replace("  ","") 
                line = line.replace("\t","")
                
                prev = curr
                curr += line #add to OBJ/BACKGROUND (key)
                x[curr] = x.pop(prev)#rewrite appended dict key
            elif line.split()[0] == "BACKGROUND":
                line = line.replace("BACKGROUND","")
                line = line.replace("\n","")
                line = line.replace("  ","") 
                line = line.replace("\t","") 

                prev = curr
                curr += line
                x[curr] = x.pop(prev)
            elif "###" in line.split()[0]:#NEW PAPER
                x[line.split()[0] + " "] = ""#set new dict for curr
                curr = line.split()[0] + " "

    with open("output.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Objective/Background", "Methods", "PMID"])

        for key, value in x.items():
            pMID = key.strip().split()[0] #first word in key
            pMID = pMID.replace("###","") 
            key = key.replace("###" + pMID + " ", "") #remove pMID from key
            writer.writerow([key, value, pMID])