
# Visualizing WhatsApp Chats

## Idea
I will continue to work on visualising the personal WhatsApp Chat Messages. I have re-used the function generating a tf-idf matrix from the previous blog post. 


## Data

For the previous blog post I have grouped the messaged by sender, so that I've had 14 documents with all messages from one person per document. 
This time, a document is a one message. I've used messages from 5 chats, so I have 5 targets or labels for my data: 'anonymous {number}', where number = 0 through 4.

## Goals

**What we have**: matrix with dimensions (1288, 369).   
Each row is a text message represented as a vector. The length of vector is the length of our vocabulary. Each vector consists of numbers, which represent the tf-idf scores for every token in a message. The vast majority of the scores are 0, because only few of the vocabulary tokens are present in a given message.

**What we want**: to reduce the dimensionality to (1288, 2). This way, each message will be described in only two numbers. 

To achieve this I will compare two dimensionality reduction techniques: tSNE and UMAP.


## Walkthrough

### tSNE

I used Yellowbrick module to apply tSNE and visualize the tf-idf matrix. 
Different colours represent different chats. We can see that there is one blog and quite a few points that surround the blog in all directions. We can see that there are no clear distinction in vocabulary between different chats.

![myplot](https://user-images.githubusercontent.com/25862134/56963786-0c5a8b80-6b5a-11e9-8166-c3dbb8691fe1.png)

### UMAP
Next I applied UMAP dimensionality reduction. For visualising the matrix I used plotly. 
The colours represent the different chats.

> If you click on the graph, you will be redirected to the plotly website where you can hover over different points and see to which chat a message belongs. 

<div>
    <a href="https://plot.ly/~gigi_karlo_/16/?share_key=Oy8NL8XQip9HO5375uPnEK" target="_blank" title="2d_reduced" style="display: block; text-align: center;"><img src="https://plot.ly/~gigi_karlo_/16.png?share_key=Oy8NL8XQip9HO5375uPnEK" alt="2d_reduced" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="gigi_karlo_:16" sharekey-plotly="Oy8NL8XQip9HO5375uPnEK" src="https://plot.ly/embed.js" async></script>
</div>


### 3d

The I experimented with 3d graphs. I saved the embeddings in an numpy file and loaded it whenever I had to plot them.

The following 3d graph shows:  
x and y: the reduced representation of a message. 
z: message length. 
text: from which chat the message is

We can see that there are a few messages around 400 characters, then there is a large gap and a couple of very long messages with anonymous 1. 

<div>
    <a href="https://plot.ly/~gigi_karlo_/12/?share_key=KwSMEELaRFYvBQBld7POJ8" target="_blank" title="3dplot_02" style="display: block; text-align: center;"><img src="https://plot.ly/~gigi_karlo_/12.png?share_key=KwSMEELaRFYvBQBld7POJ8" alt="3dplot_02" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="gigi_karlo_:12" sharekey-plotly="KwSMEELaRFYvBQBld7POJ8" src="https://plot.ly/embed.js" async></script>
</div>



Then I changed the 'colour' parameter to correspond to different chats. There seem to be little difference between what chat it is and how long the messages are.

<div>
    <a href="https://plot.ly/~gigi_karlo_/14/?share_key=lKLpt7VNDLZeRG9ic65auL" target="_blank" title="3dplot_03" style="display: block; text-align: center;"><img src="https://plot.ly/~gigi_karlo_/14.png?share_key=lKLpt7VNDLZeRG9ic65auL" alt="3dplot_03" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="gigi_karlo_:14" sharekey-plotly="lKLpt7VNDLZeRG9ic65auL" src="https://plot.ly/embed.js" async></script>
</div>



The last graph has the following axes:
x and y is the representation of a message
z is a chat a message belongs to. 
The interesting thing here is that the representations of messages in chats (the x and the y axes) are very similar. However, there are some prominent outliers. 

<div>
    <a href="https://plot.ly/~gigi_karlo_/10/?share_key=tlDaskJBY1yVKpscwL0HFk" target="_blank" title="3d-scatter-colorscale" style="display: block; text-align: center;"><img src="https://plot.ly/~gigi_karlo_/10.png?share_key=tlDaskJBY1yVKpscwL0HFk" alt="3d-scatter-colorscale" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="gigi_karlo_:10" sharekey-plotly="tlDaskJBY1yVKpscwL0HFk" src="https://plot.ly/embed.js" async></script>
</div>


## Ideas for Future Explorations

Due to time constraints I did not sufficiently discuss the meaning of the representations. Also, I might have to stop using my personal data for the assignments, since I can't go beyond the analysis of the meta data. It would've been far more interesting to actually show you which messages are outliers and discuss why that might be so. 