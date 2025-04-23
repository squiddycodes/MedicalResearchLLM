# MedicalResearchLLM
Fine tuned Medical Research paper generating LLM, trained on 200,000 medical research paper abstracts categorized by Objective/Background Statements, and Methodology statements

* **processPaperData.py** generates the train, test and validation datasets for the use of training and evaluating the model, given the large input dataset.txt file location. The datasets are curated as Objective-Methodology key-value pairs. Data is shuffled to ensure randomness in sample.
