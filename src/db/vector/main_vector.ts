/* A vector DB class

- Embeddings, pipelines etc as methods

*/

import dotenv from 'dotenv';
import { } from 'embeddings';
import { } from 'models';
import { } from 'qdrant_async';

dotenv.config({path: 'db.env'});

function selectEmbeddingModel(): EmbeddingModel | null {
  const modelName = process.env.EMBEDDING_MODEL;

  if (!modelName) {
    console.error("EMBEDDING_MODEL environment variable is not set.");
    return null;
  }

  const selectedModel = embedding_models.find(model => model.name.toLowerCase() === modelName.toLowerCase());

  if (!selectedModel) {
    console.error(`Embedding model ${modelName} not found.`);
    return null;
  }

  return selectedModel;
}

// Example usage
const selectedModel = selectEmbeddingModel();
if (selectedModel) {
  console.log(`Selected Embedding Model: ${selectedModel.name}`);
  console.log(`Model Key: ${selectedModel.key}`);
  console.log(`Model: ${selectedModel.model}`);
  console.log(`Dimensions: ${selectedModel.dim}`);
  console.log(`Usage: ${selectedModel.usage}`);
}
