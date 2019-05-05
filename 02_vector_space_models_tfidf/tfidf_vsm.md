## Idea and Inspiration

In this blog post I am quantifying my own online social interactions. The general idea of _quantified self_ has its roots in a [video by Kurtis Baute](https://youtu.be/0tnX81N6Ris) in which he talks about tracking many areas of his life and then making sense of the data. For now, I am just going to explore the text archives from 14 WhatsApp conversations, which I have been part of.

There are two major stops on this journey:   

1. Visualising TF-IDF weights for each conversation and hence the most significant distinguishing words for each.   
2. Visualising the usage of emojis in chats over time. 

Note on privacy: the messages themselves as well as the identities of conversants will remain undisclosed. 


## Data Preprocessing

I've started with 10395 messages. Since I am only interested in textual data, I removed messages containing information about omitted media as well as end-to-end encryption notifications. This resulted in a total number of 9250 messages. 

The data was not particularly messy, so I've only changed the words to lower case as a cleaning step. Stemming and lemming of data did not have any significant impact on the data, so I decided not to use it for now.

At this stage the data frame contained the following columns:

`['index', 'date', 'name', 'msg', 'msg_len'] `

The boxplot of the distribution of message lengths tells us that interquartile range is between 44 and 77 characters with the median of 53 chars. Here, the median is probably a more accurate representation of a central metric than the mean of 58 chars: the outliers skew the mean of data a little bit towards the upper limit.

![message_len_boxplot](https://user-images.githubusercontent.com/25862134/56561986-a6459580-65a8-11e9-9a52-aebe90a12c99.png)


## TF-IDF

The question I aimed to answer first was: which words appear often in a given conversation, but not as often as in all other ones? For this I have grouped all messages from one person into one array: each array can therefore be considered a document. In total I've composed 15 documents: 14 from the messages from other people, and the 15th from my responses.


With [sklearn Tfidf Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) I've transformed the data into a sparse matrix. Only the words that appeared in the document more than 3 times were taken into account: this way I significantly reduced the dimensionality of my matrix. German stop-words were removed.

### TF-IDF Visualization

For initial visualisations I've used [Tableau Public](https://public.tableau.com/s/). Below are a few **Treemaps** of TF-IDF score distributions for different conversations. The specificity of each graph does strongly suggest that TF-IDF with stop-words removed did an acceptable job of finding the important words for each individual conversation.

![anonymous_05](https://user-images.githubusercontent.com/25862134/56545198-176c5500-6577-11e9-94a5-d0f979fb9a45.jpeg)
![anonymous_12](https://user-images.githubusercontent.com/25862134/56545199-1804eb80-6577-11e9-9316-2bc1430093d8.jpeg)
![anonymous_15](https://user-images.githubusercontent.com/25862134/56545200-1804eb80-6577-11e9-86e4-dfc8e90008a3.jpeg)

To demonstrate how the TF-IDF Vectorizer would behave if only stop-words of one language were removed, however two languages were used in a conversation, I have also visualized one conversation out of the 14 which was sometimes in English and sometimes in German. The English words were unique to this conversation, hence considered important to the context. 

![anonymous_english](https://user-images.githubusercontent.com/25862134/56545201-1804eb80-6577-11e9-9a93-ea166b1398fd.jpg)

An alternative visualization technique would be **Packed Bubbles**. I find the small differences in scale of tfidf weights to be less clear here.

![mirja_03_tfidf](https://user-images.githubusercontent.com/25862134/56545572-4afbaf00-6578-11e9-8f70-f51bdbda2d15.jpg)

## Date and Length of Messages Received

Next I have plotted a **Contour Plot** of date VS length of messages for all conversation between April 2017 and April 2019. This has been an interesting insight into when I spend a lot of time chatting with people online. 

For all plots below I've used the [RawGraphs](rawgraphs.io) visualisation tool.

![date_msg_length](https://user-images.githubusercontent.com/25862134/56546143-f1947f80-6579-11e9-840c-e9caedf42025.jpg)


## Emojis

To visualize how many emojis are used in individual messages I've used the _Counter_ from the collections library as well as the _emoji_ library. For the plots below I've only taken top 50 most used emojis into account, otherwise my matrices became too large. The **Circular Denrogram** does reflect the truth: there are not many emojis in my whatsapp messages.

![len_emoji_circle](https://user-images.githubusercontent.com/25862134/56546912-0e31b700-657c-11e9-806e-57cee7e51e52.jpg)

The **Streamgraph** visualizes the use of emojis for the time range between last April and now.

![emoji_01](https://user-images.githubusercontent.com/25862134/56546600-28b76080-657b-11e9-835d-f028c1a38e4c.jpg)


The next question I asked myself was: how does the length of the message relate to the number of emojis? The pattern below is quite clear: the shorter the message - the more emojis. 

![len_emoji_msg_len](https://user-images.githubusercontent.com/25862134/56546991-4d600800-657c-11e9-98da-6f8212e4bcd9.jpg)

## Future Work

There are plenty of possibilities to further explore the WhatsApp data I have gathered. Some of these are: 

- Learning D3.js to code my own beautiful graphs ( RawGraphs are built on top of it )
- Preprocessing: another go at lemming, stemming of data
- Emoji: Chat-by-chat investigation, network graphs of people who I use similar emojis with
- Dimensionality Reduction: the majority of values in matrices are zero
- Your suggestions?

# References


1. Visualisation Tools:
    - [RawGraphs](rawgraphs.io)
    - [Tableau Public](https://public.tableau.com/s/)
2. [sklearn Tfidf Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)


