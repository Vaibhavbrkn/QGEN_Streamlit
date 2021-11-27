# QGEN_Streamlit: Question Generation APP powered by Streamlit.

## ✨ Features

- **Generate MCQ from passage with options.**
- **Generate Fill in Blank Question.**

## 🚀 Quickstart

> First download the [sense2vec weight](https://pypi.org/project/sense2vec/). Unzip it and place it into a path.

```bash
pip install -r requirements.txt
```

````python
streamlit run app.py
````

## 🐳 DOCKER
> App can be launched with Docker too.
- **Pull Docker Image from Hub**

```bash
docker pull vaibhavbrkn/nlp-question
```

- **Run Image**

```bash
docker run -p 8501:8501 vaibhavbrkn/nlp-question
```

- **Run With Kubernetes**

```bash
kubectl apply -f k8s
```

## DEMO

![Demo Image](https://github.com/Vaibhavbrkn/QGEN_Streamlit/blob/master/demo.jpg)
