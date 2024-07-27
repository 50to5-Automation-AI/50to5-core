/* Embeddings

Include a selection including in the front end and find the dimensions to
set as a dictionary
- sentence embeddings Dim:
- snowflake embeddings Dim:
- OpenAI embeddings: Dim: 
- Word2Vec embeddings: Dim:

Make a constructor for choosing embedddings and setting dim with an array

*/


import { OpenAIEmbedding, Settings } from "llamaindex";
import { MistralAIEmbedding } from "llamaindex";
import dotenv from 'dotenv';

dotenv.config({path='../../db.env'});

//Main?
export async function(name: string) {
    function set_embeddings(name: string) {
        Settings.embedModel = new OpenAIEmbedding({
            model: "text-embedding-ada-002",
        });
    }

// MistralAI Embedding
export async function mistral_embeddings(data: JSON) {
    Settings.embedModel = new MistralAIEmbedding({
    apiKey: process.env.MISTRAL_API_KEY,
    });

    const document = new Document({ text: essay, id_: "essay" });
    const index = await VectorStoreIndex.fromDocuments([document]);
    const queryEngine = index.asQueryEngine();
    const query = "What is the meaning of life?";
    const results = await queryEngine.query({
    query,
    });
}

//@TODO FIX OPEN AI

