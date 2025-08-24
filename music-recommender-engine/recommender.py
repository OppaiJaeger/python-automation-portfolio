# Import all necessary libraries for the project
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the path to the dataset file.
# The 'r' before the string creates a raw string to handle backslashes correctly.
file_path = r'spotify_millsongdata.csv'

# Download NLTK data (stopwords and punkt) if not already downloaded.
# This is a one-time setup step required for text preprocessing.
try:
    _ = stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
try:
    _ = nltk.word_tokenize("test")
except LookupError:
    nltk.download('punkt')
    
# Load the dataset into a pandas DataFrame.
# A try-except block is used for robust file handling.
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
    
# Sample the DataFrame to a smaller, more manageable size (e.g., 5000 songs).
# This is a professional and practical approach to handle large datasets and avoid MemoryError.
# random_state ensures the sample is the same every time for reproducibility.
df = df.sample(n=5000, random_state=42).reset_index(drop=True)

# Check for and handle any missing values in the 'text' column, which are critical for the model.
df.dropna(subset=['text'], inplace=True)

# Define the text preprocessing function.
# This function cleans and standardizes the song lyrics for analysis.
def preprocess_text(text):
    """
    Cleans and preprocesses a string of text for natural language processing (NLP).

    The function performs a series of operations to prepare the text:
    1. Converts text to lowercase.
    2. Removes all punctuation.
    3. Tokenizes the text into a list of words.
    4. Removes common English stop words.
    5. Applies stemming to reduce words to their root form.

    Args:
        text (str): The raw text string to be processed.

    Returns:
        str: The processed text as a single string of stemmed words.
    """
    # Create a translation table to delete all punctuation characters
    translator = str.maketrans('', '', string.punctuation)
    
    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove all punctuation using the translation table
    text_without_punctuation = text.translate(translator)

    # Initialize stop words and stemmer outside the function for efficiency
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # 3. Tokenize the text using NLTK's word_tokenize
    tokens = nltk.word_tokenize(text_without_punctuation)

    # 4. & 5. Remove stop words and apply stemming in a single list comprehension
    processed_tokens = [
        stemmer.stem(word) for word in tokens if word not in stop_words
    ]

    # Join the processed tokens back into a string
    return " ".join(processed_tokens)

# Apply the preprocessing function to the 'text' column to create a new 'processed_text' column.
# The .apply() method is a highly efficient way to run a function on a pandas Series.
df['processed_text'] = df['text'].apply(preprocess_text)

# Initialize the TfidfVectorizer.
# This tool handles tokenization and TF-IDF calculations in a single, optimized step.
vectorizer = TfidfVectorizer()

# Fit and transform the processed text to create the TF-IDF matrix.
# This matrix is the numerical representation of the song lyrics.
tfidf_matrix = vectorizer.fit_transform(df['processed_text'])

# Compute the cosine similarity matrix.
# This matrix contains the similarity score between every pair of songs.
cosine_sim = cosine_similarity(tfidf_matrix)

# Define the main recommendation function.
def get_recommendations(song_title, cosine_sim):
    """
    Generates a list of song recommendations based on lyrical similarity.

    The function finds songs with similar lyrical content to a given song
    by using a pre-computed cosine similarity matrix.

    Args:
        song_title (str): The title of the song to get recommendations for.
        cosine_sim (np.ndarray): The pre-computed cosine similarity matrix.

    Returns:
        list: A list of recommended songs, with each song represented as a
              Pandas Series containing its information. Returns an empty list
              if the song is not found.
    """
    # Find the index of the song that matches the title
    # .tolist() is used to convert the Index object to a simple list
    song_indices = df.index[df['song'] == song_title].tolist()

    # Check if the song was found in the DataFrame
    if not song_indices:
        print(f"Song '{song_title}' not found in the dataset.")
        return []

    # Get the similarity scores for the chosen song from the cosine similarity matrix
    # [0] is used to get the single index from the list
    sim_scores = cosine_sim[song_indices[0]]

    # Get the indices of the songs sorted by similarity score in descending order
    # np.argsort returns the indices that would sort the array
    # reversed() is used to get them from most to least similar
    sorted_indices = np.argsort(sim_scores)
    
    # Use a list comprehension to filter out the input song's own index.
    # The list comprehension is a more efficient and "Pythonic" way to do this.
    rec_indices = [
        index for index in reversed(sorted_indices)
        if index != song_indices[0]
    ]

    # Take the top 10 recommendations from the filtered list
    top_10_rec = rec_indices[:10]

    # Use a list comprehension to retrieve the actual songs from the DataFrame.
    # df.iloc[i] is used to get the entire row (song) by its integer index.
    recommended_songs = [
        df.iloc[i] for i in top_10_rec
    ]

    return recommended_songs

# Define the main function to handle user interaction.
def main():
    """
    Serves as the main user interface for the music recommendation engine.
    It prompts the user for a song, calls the recommendation function,
    and displays the results.
    """
    print("\nWelcome to the Music Recommendation Engine!")
    print("\nNote: The model was trained on a sample of 5000 songs, so not all songs are available.")
    print("\nFor a successful test, try these titles: 'Love', 'Happy', or 'Blue'.")
    
    song_title = input("\nPlease Enter Song Title: ")

    # Use a try-except block to handle cases where the song is not in the DataFrame
    try:
        artist_name = df.loc[df['song'] == song_title, 'artist'].item()
        print(f"\nYou entered the song '{song_title}' by {artist_name}")
    except (KeyError, IndexError):
        # The get_recommendations function will handle this case gracefully.
        pass

    # Call the get_recommendations function
    rec_list = get_recommendations(song_title, cosine_sim)

    # Print the results in a readable format
    if rec_list:
        print("\nHere are your recommendations:")
        for i, rec_song in enumerate(rec_list, 1):
            print(f"{i}. {rec_song['song']} by {rec_song['artist']}")
    else:
        print("Please try a different song title.")

# Standard Python practice to run the main function when the script is executed.
if __name__ == "__main__":
    main()