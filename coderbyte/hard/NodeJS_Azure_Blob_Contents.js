// Node.js Azure Blob Contents
// Given a container name and a blob name, return the contents of the blob.
// For example, given the container name "mycontainer" and the blob name "myblob", return the contents of the blob "myblob" in the container "mycontainer".
// If the blob does not exist, return "Blob not found".
// If the container does not exist, return "Container not found".
// If the blob exists but is empty, return "Blob is empty".
// If the container exists but the blob does not exist, return "Blob not found".

// Examples
// Input
// container = "mycontainer"
// blob = "myblob"

// Output
// "Hello, world!"

// Input
// container = "mycontainer"
// blob = "myblob"

// Output
// "Blob not found"

const { BlobServiceClient } = require("@azure/storage-blob");
require("dotenv").config();

const container = "mycontainer";
const blob = "myblob";

async function getBlobContents(container, blob) {
    const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING;
    const blobServiceClient =
        new BlobServiceClient(connectionString);
    const containerClient = blobServiceClient.getContainerClient(container);
    const blobClient = containerClient.getBlobClient(blob);

    try {
        const response = await blobClient.download();
        const contents = await streamToString(response.readableStreamBody);
        return contents;
    } catch (error) {
        if (error.statusCode === 404) {
            if (error.details.errorCode === "BlobNotFound") {
                return "Blob not found";
            } else if (error.details.errorCode === "ContainerNotFound") {
                return "Container not found";
            }
        }
        throw error;
    }
}

getBlobContents("mycontainer", "myblob");

async function streamToString(readableStream) {
    return new Promise((resolve, reject) => {
        const chunks = [];
        readableStream.on("data", (data) => {
            chunks.push(data.toString());
        });
        readableStream.on("end", () => {
            resolve(chunks.join(""));
        });
        readableStream.on("error", reject);
    });
}
