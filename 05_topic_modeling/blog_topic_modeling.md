# Topics of Datasets on Kaggle
> **Date:** 14.05. *(Due: 14.05.)*  
> **Name:** `AlVy` Alyona Vyshnevska  
> **Session:** [Introduction](../index)   
> **Code:** [here]()   

----


Let's find out if we can group descriptions of Kaggle datasets by topics. 


### Dataset

Upvoted Kaggle datasets, collected on 21 Feb 2018. 2885 datasets. The visualisation used later on could not cope with the number of documents (descriptions).  
Therefore, I have taken a subset of the dataset: 100 documents.

### Data Pre-Processing

- Remove stop words: extend stop words with words that are common in all documents. These appear as important words for the topics,
however they do not convey any interesting information for our purposes.

### Train model
- Number of topics: 10 (arbitrary choice)
- Save model for later use 

### Discuss
So what do we observe?

There are several clusters: 
- 1 cluster with three topics
- 3 clusters with two topics 
- single topic

Overall, most salient terms are:
- disagree
- interested
- enjoy
- agree
- health
- bitcoin

Per topic:



### Future Work

With removing words common to all topics I practically tried what tf-idf does. I did not find a way to utilize tf-idf within gensim LDA model training, however I have not found it. 



