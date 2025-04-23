# MedicalResearchLLM
This project is a Fine tuned Medical Research paper generating LLM, trained on 3,200 medical research paper abstracts categorized by Objective/Background Statements, and Methodology statements. 

This project uses LLama 3.1 (8B) and LoRA, and is fine tuned using Unsloth. Read about our methodology, design choices and implementation process in **Report.pdf!**

# Dataset Curation
* **dataset.txt** is used by the .py file - set the filepath to the filepath of your downloaded dataset.txt to generate the csvs for the model evaluation.
* **processPaperData.py** generates the train (3200 rows), test (400 rows), validation (400 rows), and human feedback (10) csvs used for the training and evaluation of the model, given the large input dataset.txt file location. The datasets are curated as Objective-Methodology key-value pairs. Data is shuffled to ensure randomness in sample.

# Model Training
We trained this model using Unsloth's Google Colab for Llama 3.1, connecting to the free T4 Colab offers. We made changes to how the data prep and training code blocks, and have our own code blocks for inferences made by the model. To run this for yourself, visit https://colab.research.google.com/drive/1RDfwQziQzwzE8qC7XTTpygdutJ237X_9#scrollTo=CYg-eV0vkBJt

After cloning the Colab to your drive, you can create folder *data* and place the csvs you generated into the folder. This will align with our Data Prep code in Colab pointing to your drive, mounting at *content/drive/MyDrive/data/train.csv* and the other 3 csvs. Ensure all 4 csvs (train, validation, test, humanFeedback) are in the *data* folder in your drive before running the Colab code. 

After the csvs are in *data*, you can run the code blocks in order, and see the results! You can test inferences after the model trains, to see for yourself how the model performs! Details on our project's results are in **Report.pdf**.
