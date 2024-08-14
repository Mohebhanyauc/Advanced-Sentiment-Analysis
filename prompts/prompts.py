TEST_PROMPT="""
Gather all your energy and concentrate of this problem. 

1- I will give you a social media comment, the primary language of it is Arabic, but it may include some English words, so focus on every word in it.
You should understand the context of the sentense really well. 

2- classify this comment into only one of the following 4 catigories: neutral, positive, negative, mixed. 
Imagive we have an axis that is named "feelings".
Return "positive: if the commenter  has a positive feeling.
Return "negative" if the commenter has a negative feeling.
Return "neutral" if the commenter has zero feeling. 
Return "mixed" if the commenter mentions that he has a positive and a negative feeling in the same comment. 

3-Understand, by understanding the context and knowing the sentement you should tell me the reason why you chose this sentement.  
Reasons should be short and staight to the point. 
For example : 'Slow delivery of burgers' or 'bad preformance in ads'
Only return the sentement with its reasoning in JSON fromat.
Stick to the following format:

'sentiment': '',
'reason': ''

Here is the comment: {comment}

Take a deep breath, if you do well I will tip you $200.
"""

