# ChatBot with Flask
Chatbot in python using Flask


Our Bot uses an offline backend corpus as a knowledge base which user can change by merely tweaking the backend corpus by adding their personalization to answers from Bot. It is a simple command-line implementation for beginners, but to make it look interesting will be adding things like emotion detection, greeting function, and a color pallet to distinguish between questions and answers.



## Installation



### Docker 

Install Docker desktop  [here](https://www.docker.com/products/docker-desktop)

and then in your terminal 

```
docker pull ruslanmv/chatbot:latest
```

go to  your browser

```
http://localhost:5000/
```

### Local

Install anaconda, and  follow the next steps in the cmd terminal

```
conda create -n chatbotweb python==3.7
```

```
conda activate chatbotweb
```

```
git clone https://github.com/ruslanmv/chatbot
```

```
cd chatbot
```

```
pip install -r requirements.txt
```

If you are in windows  you should have admin privileges

```
python -m spacy download en
```

```
phyton app.py
```

go to  your browser

```
http://localhost:5000/
```

### Docker Local

```
git clone https://github.com/ruslanmv/chatbot
```

```
docker build --tag flask-chatbot-app .
```

```
docker run -i -t --name flaskpltapp -p5000:5000 flask-chatbot-app:latest
```

go to your browser

```
http://localhost:5000/
```

