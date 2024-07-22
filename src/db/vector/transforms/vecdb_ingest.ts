import fs from "node:fs/promises";

import {
  Document,
  IngestionPipeline,
  MetadataMode,
  OpenAIEmbedding,
  TitleExtractor,
  SimpleNodeParser,
  QdrantVectorStore,
  VectorStoreIndex,
} from "llamaindex";

async function main() {
  // Load essay from abramov.txt in Node
  const path = "node_modules/llamaindex/examples/abramov.txt";

  const essay = await fs.readFile(path, "utf-8");

  const vectorStore = new QdrantVectorStore({
    host: "http://localhost:6333",
  });

  // Create Document object with essay
  const document = new Document({ text: essay, id_: path });
  const pipeline = new IngestionPipeline({
    transformations: [
      new SimpleNodeParser({ chunkSize: 1024, chunkOverlap: 20 }),
      new TitleExtractor(),
      new OpenAIEmbedding(),
    ],
    vectorStore,
  });

  // run the pipeline
  const nodes = await pipeline.run({ documents: [document] });

  // create an index
  const index = VectorStoreIndex.fromVectorStore(vectorStore);
}

main().catch(console.error);