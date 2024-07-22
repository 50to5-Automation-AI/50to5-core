interface EmbeddingModel {
    name: string;
    key?: string;
    model: string;
    dim: number;
    usage: string;
  }
  
  const embedding_models: EmbeddingModel[] = [
    {
      name: "OpenAI",
      key: process.env.OPENAI_API_KEY,
      model: "text-embedding-ada-002",
      dim: 1536,
      usage: "General-purpose text embeddings with high dimensionality for detailed representations."
    },
    {
      name: "Snowflake",
      model: "text-embedding-xyz",  // Replace with actual model name
      dim: 512,  // Replace with actual dimension
      usage: "Optimized for database query embeddings and analytics."
    },
    {
      name: "MistralAI",
      model: "text-embedding-mistral",  // Replace with actual model name
      dim: 768,  // Replace with actual dimension
      usage: "Specialized for scientific and research paper embeddings."
    },
    {
      name: "Word2Vec",
      model: "word2vec-google-news-300",
      dim: 300,
      usage: "Efficient for word-level embeddings and NLP tasks."
    },
    {
      name: "HuggingFace",
      model: "distilbert-base-uncased",
      dim: 768,
      usage: "Compact and efficient text embeddings suitable for NLP tasks."
    }
  ];
  