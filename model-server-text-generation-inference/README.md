# Substratus ModelServer Basaran Image

This image can be used for a model server to serve huggingface models.

The image expects a huggingface model under the /model/saved/ directory.

## Usage for testing

### Building
Build the image:
```sh
docker build -t substratusai/model-server-basaran .
```

### Running a test
Download a specific model:
```
docker run -e PARAMS_NAME=facebook/opt-125m \
  substratusai/model-loader-huggingface:latest
```
### Running notebook in container
This is helpful to test out the loader while developing

Run Jupyter Notebook mounting local src directory:
```
docker run -it -p 8888:8888 \
  -v $(pwd)/load.ipynb:/model/src/load.ipynb \
  substratusai/model-loader-huggingface notebook.sh
```

You can then access Jupyter Lab by visiting:
[http://localhost:8888](http://localhost:8888).

You will see a notebook called train.ipynb under the src directory. You can modify that
that notebook as needed and run it to fine tune the model.
