FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install sentencepiece
EXPOSE 8501
COPY . /app 
RUN python -m nltk.downloader stopwords
RUN python -m spacy download en_core_web_sm    
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
