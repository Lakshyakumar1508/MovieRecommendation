# Movie Recommendation System using Machine Learning
This project is a Movie Recommendation System built using machine learning techniques. The system utilizes a dataset containing information about 5000 movies, including attributes such as movie name, budget, genre, keywords, overview, popularity score, production companies, production countries, revenue, cast, crew, etc.

# Trying the Application
Anyone can use the program using this site!

https://movie-recommendation-system-using-ml-5cpthldm5cqry8ghu3qv4n.streamlit.app/


## Dataset
The dataset used for this project contains a comprehensive set of attributes for each movie, allowing for a thorough analysis and recommendation process. However, to streamline the model creation process, only essential columns were selected for building the recommendation system.

## Preprocessing
Prior to model creation, the dataset underwent preprocessing to clean and organize the data. This involved handling missing values, standardizing formats, and selecting relevant features necessary for the recommendation algorithm.

## Model Building
The recommendation system employs cosine similarity to identify the most similar movies to a given movie. By computing the cosine similarity between movie vectors, the system can effectively determine which movies are closely related based on their features.

## Streamlit Application
To provide users with an interactive experience, a Streamlit application was developed. This application utilizes the preprocessed dataset and the cosine similarity model to recommend movies. Users can input a movie title, and the application will return the names and posters of the five most similar movies. For fetching movie posters, the OMDB API was integrated into the application. This allows the system to display posters alongside the recommended movie titles, enhancing the user experience.

## Acknowledgments
Special thanks to the creators of the dataset and the OMDB API for providing valuable resources for this project. Additionally, gratitude is extended to the Streamlit team for developing a user-friendly framework for building interactive applications.

## Contribution
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
