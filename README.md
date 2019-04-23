# Quantifying Social Self

When it comes to social interactions there is a clear hierarchy for me: in person before messaging before calls. Quantifying in-person conversation is a hustle, but taking a peek at my interactions with others on WhatsApp is easy: WhatsApp allows for chat exports. 

### Why exploring personal WhatsApp chats can be interesting? 

Quantifying our interactions with others can give us insights about ourselves and find out how situational I behave. 

- How many and which emoji do I use with different people?
- How steady are the interactions with different people? 
- Does the vocabulary differ? If not, do the words _mean_ the same in different contexts? 

![communicating](https://user-images.githubusercontent.com/25862134/56571154-a2237300-65bc-11e9-855b-22e52fd11469.png)

### Areas to Explore

1. Most commonly used words/emojis 
    - TF-IDF is a good candidate for analysing the words importance to a particular conversation
2. The steadiness of contact over time
    - Graphing long breaks between interactions or times when I was in contact with a person significantly more than usual 
3. Topic Modelling 
    - What do I actually talk about with people? Are there many overlaps? Are there people, with whom my conversations differ significantly from everybody else?
4. Meaning of words: what other words are used in same contexts? 

### (Possible) Goals

As a possible target for the project one could aim to create Word Embeddings for the data and explore the _blank_ to _blank_ is as _blank_ to _what_ kinds of questions. One could play around with the perplexity value, which in the context of t-SNE (a nonlinear dimensionality reduction technique)is a smooth measure of the effective number of neighbours.

![word-2-vec](https://user-images.githubusercontent.com/25862134/56568849-23c4d200-65b8-11e9-9d51-f2af1d9b8c54.gif)

Alternatively, one could create and explore a network graph of topics that I am talking about with people. What would be really interesting is to graph branching out of topics to see with whom I often go off-topic. Below is a graph from an [analysis of a Reddit thread](https://blog.embed.ly/visualizing-discussions-on-reddit-with-a-d3-network-and-embedly-e3ac9297bebd) and how the topics branch out: 

![branching_reddit](https://user-images.githubusercontent.com/25862134/56568331-0ba08300-65b7-11e9-9feb-d92a35b949d0.png)



## References

- [This blog post](http://ml4ma.blogspot.com/2015/11/a-guide-to-extract-whatsapp-chat-log.html) has been an inspiration for data pre-processing and ideas on what to do with the data/. 