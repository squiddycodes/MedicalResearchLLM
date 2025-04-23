import csv
import random
fileName = r"C:\Users\dguid\Desktop\200k_abstracts\train.txt"#txt file containing the 
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

    dataset = list(x.items())
    random.shuffle(dataset) #for randomness
    with open("train.csv", "w", newline="", encoding="utf-8") as trainFile, \
     open("test.csv", "w", newline="", encoding="utf-8") as testFile:
        trainWriter  = csv.writer(trainFile)
        testWriter = csv.writer(testFile)

        for i, (key, value) in enumerate(dataset):
            pMID = key.strip().split()[0] #first word in key
            pMID = pMID.replace("###","")
            key = key.replace("###" + pMID + " ", "") #remove pMID from key

            if i < 500:
                trainWriter.writerow([key, value])
            elif i < 510:
                testWriter.writerow([key, value])
            else:
                break