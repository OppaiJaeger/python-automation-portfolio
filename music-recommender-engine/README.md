# Music Recommendation Engine

A data-driven project that builds a simple content-based recommendation system using Python and the Pandas library. The system analyzes the lyrical content of songs to recommend similar music.

## Features

- **Data Handling**: Efficiently loads and processes [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset) using Pandas.
- **Text Preprocessing**: Cleans and prepares raw text data by removing punctuation, stop words, and applying stemming.
- **TF-IDF Vectorization**: Converts lyrical content into a numerical format for analysis.
- **Cosine Similarity**: Calculates the similarity between songs to find the most relevant recommendations.
- **User Interface**: A simple command-line interface to get user input and display recommendations.

## Methodology

This project follows a standard content-based filtering pipeline.

1.  **Data Preprocessing**: Lyrical content is cleaned and standardized using a custom function that removes punctuation, filters out common stop words, and applies stemming to reduce words to their root form.
2.  **Vectorization**: The processed lyrics are converted into a numerical matrix using the **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorizer. This method assigns a numerical weight to each word, reflecting its importance in a song's lyrics.
3.  **Similarity Calculation**: The similarity between each song is calculated using **Cosine Similarity**, a metric that measures the cosine of the angle between two TF-IDF vectors.
4.  **Recommendation Logic**: The system takes a song as input, finds its most similar songs from the similarity matrix, and returns the top-N recommendations.

## File Structure

```text

music_recommender_engine/
├── music_recommender_analysis.ipynb # Main project notebook
├── requirements.txt # Requirements to install
├── LICENSE.md # MIT licence
└── README.md # Project documentation

```

## Dependencies & Setup

This project requires the following Python libraries, which can be installed using pip:

```bash
pip install -r requirements.txt
```

In addition to the libraries, this project uses specific data from the nltk library. You must download this data separately by running the following commands in a Python environment (like the Jupyter Notebook):

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Usage

To run the project, navigate to the music_recommender_engine directory and open the terminal.

```bash
pip install -r requirements.txt
jupyter notebook music_recommender_analysis.ipynb
```

## Acknowledgements

I would like to thank the provider of the [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset) on Kaggle. This project would not have been possible without this well-structured and comprehensive dataset.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
