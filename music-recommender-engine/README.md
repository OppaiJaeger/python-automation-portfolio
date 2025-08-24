# Music Recommendation Engine

A data-driven project that builds a simple content-based recommendation system using Python and the Pandas library. The system analyzes the lyrical content of songs to recommend similar music.

## Features

- **Data Handling**: Efficiently loads and processes [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset) using Pandas.
- **Text Preprocessing**: Cleans and prepares raw text data by removing punctuation, stop words, and applying stemming.
- **TF-IDF Vectorization**: Converts lyrical content into a numerical format for analysis.
- **Cosine Similarity**: Calculates the similarity between songs to find the most relevant recommendations.
- **Interactive User Interface**: A simple command-line interface is available in both the notebook and the standalone script to get user input and display recommendations.

## Methodology

This project follows a standard content-based filtering pipeline.

1. **Data Preprocessing**: Lyrical content is cleaned and standardized using a custom function that removes punctuation, filters out common stop words, and applies stemming to reduce words to their root form.
2. **Vectorization**: The processed lyrics are converted into a numerical matrix using the **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorizer. This method assigns a numerical weight to each word, reflecting its importance in a song's lyrics.
3. **Similarity Calculation**: The similarity between each song is calculated using **Cosine Similarity**, a metric that measures the cosine of the angle between two TF-IDF vectors.
4. **Recommendation Logic**: The system takes a song as input, finds its most similar songs from the similarity matrix, and returns the top-N recommendations.

## File Structure

```text

music_recommender_engine/
├── music_recommender_analysis.ipynb # Main project notebook
├── recommender.py # Standalone Python script
├── outputs/
│   ├── demo.png # Notebook demo output
│   └── demo_2.png # Script demo output
├── requirements.txt # Project dependencies
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

This project can be run in two ways:

1.  **Using the Jupyter Notebook:** Navigate to the `music_recommender_engine` directory and open the notebook to see the step-by-step process.
    ```bash
    jupyter notebook music_recommender_analysis.ipynb
    ```

2.  **Using the Standalone Script:** You can also run the final recommendation engine directly from the terminal.
    ```bash
    python recommender.py
    ```


## Demo 

output of the main function in jupyter notebook :

![demo.png](https://github.com/OppaiJaeger/python-automation-portfolio/blob/main/music-recommender-engine/outputs/demo.png)

output of recommender.py :

![demo_2.png](https://github.com/OppaiJaeger/python-automation-portfolio/blob/main/music-recommender-engine/outputs/demo_2.png)

## Acknowledgements

I would like to thank the provider of the [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset) on Kaggle. This project would not have been possible without this well-structured and comprehensive dataset.
