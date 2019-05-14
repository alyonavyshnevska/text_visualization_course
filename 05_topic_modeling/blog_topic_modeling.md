# Topics of Datasets on Kaggle
> **Date:** 14.05. *(Due: 14.05.)*  
> **Name:** `AlVy` Alyona Vyshnevska  
> **Session:** [Introduction](../index)   
> **Code:** [here](https://github.com/alyonavyshnevska/text_visualization_course/tree/master/05_topic_modeling)   

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

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/overall_salient.jpeg?raw=true)

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

The only **outlier-topic** is best described by: interested, disagree, enjoy, agree, much, and school. Words like student and college also appear. 

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/outlier_topic_4.jpeg?raw=true)

Topic **two** and topic **eight** are positioned closely to each other and a bit further away from every other topic. They shape 2 out of 5 top words: agree and time. Otherwise, topic two is chracterized by: 

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/topic_2.jpeg?raw=true)

Topic 8 is characterized by:

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/topic_8.jpeg?raw=true)

Topic 7 is largely included in the topic 1, so one could reduce the size of topics from 10 to 9.  
The most relevant words for topic 7 are: crash, time, dub, cluster, using. Player, dollar, and movie also appear. Time and dub are also in the top five of the larger topc 1.

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/topic_7.jpeg?raw=true)

![](https://github.com/alyonavyshnevska/text_visualization_course/blob/master/05_topic_modeling/img/topic_1.jpeg?raw=true)

### Future Work

With removing words common to all topics I practically tried what tf-idf does. I did not find a way to utilize tf-idf within gensim LDA model training, however I have not found it. 



