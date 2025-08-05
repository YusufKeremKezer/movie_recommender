# Movie Recommender


AI-powered movie and TV series recommendation system with an interactive chat-based interface. Users can ask for personalized movie and TV show recommendations through a conversational interface. The system understands user preferences, mood, and genre preferences to provide tailored suggestions. It also provides additional information about movies and TV series by integrating with Wikipedia.

Key features:
- **Conversational Interface**: Chat-based UI for natural interaction
- **Personalized Recommendations**: AI understands user taste and preferences from conversation history
- **Movie Database Search**: Vector-based search through movie and TV series data
- **Additional Information**: Integration with Wikipedia for detailed movie/series information
- **Memory**: Maintains conversation history and user preferences

## Technologies Used

- **Python 3.12** - Core programming language
- **Streamlit** - Web user interface framework
- **Google Gemini 2.0 Flash** - AI language model for generating recommendations
- **LangChain & LangGraph** - AI workflow and orchestration framework
- **ChromaDB** - Vector database for movie data storage and similarity search
- **HuggingFace Embeddings** - Text embeddings using Alibaba-NLP/gte-multilingual-base model
- **Wikipedia API** - External data source for movie information
- **Docker** - Containerization platform

## Docker Hub Usage

### For Users - Pull and Run Pre-built Image

If the image is available on Docker Hub, anyone can pull and run it without building:

```bash
# Pull the image from Docker Hub
docker pull keremz/movie_recommendation_app:latest

# Run the container
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_google_api_key_here keremz/movie_recommendation_app:latest
```

