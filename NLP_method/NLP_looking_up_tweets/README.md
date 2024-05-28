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
The repository is organized as follows:
- **Folders**:
  - `__pycache__`: Contains cached Python bytecode files.
  - `data`: Stores data used by the method.
  - `images`: Holds images used in the method or tutorial.
  - `tmp2`: Contains additional files and data, including stopwords and the `twitter_samples` dataset.

- **Files**:
  - `Looking up the tweets.ipynb`: The main code implemented as a Jupyter Notebook. It contains four sections covering document embeddings, tweet lookup, similarity computation, and hash table creation..
  - `readme.md`: Guideline document providing instructions for using the method.
  - `utils.py`: Contains essential functions needed for the method's functionality.
  - `w4_unitest.py`: Unit test file to verify correct execution of the code.


## Environment Setup
Requires Python and the NLTK library. Install NLTK using:

```
pip install nltk
```


## Hardware Requirements (Optional)
No specific hardware requirements.

## Input Data
Digital Behavioral Data (DBD) Dataset, such as social media posts like Tweeter(https://data.gesis.org/tweetskb/)

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


## Acknowledgements 
Special thanks to DeepLearning.AI on Coursera for providing the assignment used in this tutorial.





