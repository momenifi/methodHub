# Method Title
Looking up the most Similar Tweets to a text

## Description
This method guides users through finding tweets that are similar to a specific text or tweet. It explains techniques for measuring text similarity and demonstrates their implementation in Python.

## Keywords
Text similarity, Tweet analysis, Locality Sensitive Hashing (LSH), Python

## Science Usecase(s)
- **Social Media Analysis**: Analyzing social media data for sentiment trends and user behavior.
- **Content Analysis**: Examining textual data for themes and linguistic patterns.
- **Cultural Studies**: Comparing cultural artifacts such as literature or music.
- **Political Science**: Understanding political discourse and public opinion.
- **Psychological Research**: Analyzing textual data from online forums or therapy sessions.

## Repo Structure
The method contains four sections covering document embeddings, tweet lookup, similarity computation, and hash table creation.

## Environment Setup
Requires Python and the NLTK library. Install NLTK using:

```
pip install nltk
```


## Hardware Requirements (Optional)
No specific hardware requirements.

## Input Data
Digital Behavioral Data (DBD) Dataset, such as social media posts.

## Sample Input and Output Data
### Input:
Here is a tweet to search in all tweets:
'#FollowFriday @France_Inte @PKuchly57 @Milipol_Paris for being top engaged members in my community this week :)'
### Output:
Here are two most similar tweets to the given tweet:
'
document contents: #ShareTheLove @oymgroup @musicartisthere for being top HighValue members this week :) @nataliavas http://t.co/IWSDMtcayt
document contents: #FollowFriday @straz_das @DCarsonCPA @GH813600 for being top engaged members in my community this week :)
'


## How to UseTo utilize this tutorial effectively, follow these steps:

1. **Install Python and Necessary Packages**:
   - Ensure that Python is installed on your system. You can download and install Python from the official website (https://www.python.org/).
   - Install Jupyter Notebook, which is a web-based interactive computing environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text. Install it using pip:
     ```
     pip install notebook
     ```

2. **Download the Folder**:
   - Download the provided folder containing the tutorial materials to your local machine. Ensure that you have extracted the contents of the folder if it is in a compressed format (e.g., .zip).

3. **Navigate to the Directory**:
   - Open a command prompt or terminal window and navigate to the directory where you have saved the downloaded folder using the `cd` command. For example:
     ```
     cd path/to/downloaded/folder
     ```

4. **Launch Jupyter Notebook**:
   - Once you are in the directory containing the tutorial materials, start Jupyter Notebook by entering the following command in the command prompt or terminal:
     ```
     jupyter notebook
     ```
   This will open Jupyter Notebook in your default web browser.

5. **Open the Notebook**:
   - In the Jupyter Notebook interface, navigate to the "Looking up the Tweets.ipynb" file and click on it to open the notebook.

6. **Run the Codes**:
   - Run each code cell in the notebook sequentially by selecting the cell and pressing Shift + Enter or using the "Run" button in the Jupyter Notebook interface.

Follow these steps to install Jupyter Notebook, download the tutorial materials, navigate to the directory, open the notebook, and execute the provided code in the Jupyter Notebook environment.


## Contact Details
For questions or feedback, contact [email address] or [social media handles].

## Publication (Optional)
N/A

## Acknowledgements (if any)
Special thanks to DeepLearning.AI on Coursera for providing the assignment used in this tutorial.




# Method Title
The title should be meaningful and easy to follow. It should reflect relevance to social science, if applicable 

## Description
- Provide a brief and clear description of the method, its purpose, and what it aims to achieve. Add a link to a related paper from social science 
domain and show how your method can be applied to solve that research question.  
For example,
4TCT is a specialized tool designed for the efficient collection of textual data from the 4chan platform. It automates the process of gathering posts from various boards, aiming to facilitate research and analysis in social science and computational linguistics.
This tool is particularly useful for analyzing online discourse, community dynamics, and trends within the 4chan ecosystem. It can support studies on topics like meme culture, information dissemination, and the impact of anonymous social media on public opinion.

## Keywords
Few keywords placed after description highlighting the nature of the method 

## Science Usecase(s)
- Include usecases from social sciences that would make this method applicable in a certain scenario. 
The use cases or research questions mentioned should arise from the latest social science literature cited in the description.
For example,
How to collect 4chan data from on political discourse from dates ..
 

## Repo Structure
- Explain the overall structure of the method, including directories, key files, and their functions.
For example,
The tool's architecture includes a src/ directory for core scripts, with requester.py handling data collection, board.py managing board-specific requests, and utils.py for auxiliary functions. Data is stored in a data/ directory created upon initiation, and documentation is available in docs/.


## Environment Setup
- Setting up the envornment to run this method locally
- Installing all the packages and libraries with specific versions required to run this method
For example, 
Requires Python 3.10.2 or 3.11.4. Suitable for environments focused on data collection and analysis.
Dependencies are listed in requirements.txt and can be installed via pip install -r requirements.txt to ensure the tool functions correctly.




## Input Data 
- The input data has to be a Digital Behavioral Data (DBD) Dataset
- You can provide link to a public DBD dataset. GESIS DBD datasets (https://www.gesis.org/en/institute/digital-behavioral-data)





