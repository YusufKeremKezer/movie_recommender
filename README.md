# Movie Recommendation app


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
- **Google Gemini 2.5 Flash** - AI language model for generating recommendations
- **LangChain & LangGraph** - AI workflow and orchestration framework
- **ChromaDB** - Vector database for movie data storage and similarity search
- **HuggingFace Embeddings** - Text embeddings using Alibaba-NLP/gte-multilingual-base model
- **Wikipedia API** - External data source for movie information
- **Docker** - Containerization platform

## Build Docker image

### For Users - 
git clone https://github.com/YusufKeremKezer/movie_recommender.git

[Download the dataset from drive](https://drive.google.com/drive/folders/1KTGdwcJglvuoTyBu9dO4JGQNvKqBhMIa?usp=sharing)

copy inside /app

```bash
# Run the compose file
docker compose --env-file .env up -d --build
```

