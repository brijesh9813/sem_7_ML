#!/usr/bin/env python
# coding: utf-8

# Program 1: Simulating a human learning pattern through simple rules
# 

# In[1]:


# Human-like learning: learning from examples (rule learning)

examples = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "potato": "vegetable"
}

def human_learn(item):
    if item in examples:
        return examples[item]
    else:
        return "Unknown item. Need more experience."

print(human_learn("apple"))
print(human_learn("carrot"))


# In[ ]:




