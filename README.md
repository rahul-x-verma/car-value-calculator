# Car Value Calculator

A couple months ago, my mom got into a minor accident driving her very old, but very reliable, Toyota Camry. 

My mom cares very little about cars as long as they get her from point A to point B. Had this accident not occurred, 
she would not consider buying a new car. However, the cost to repair her car well exceeded its value, so it felt
a little weird to put money into it - especially if it falls apart on its own accord soon anyway. 

Lastly, my mom reckoned that a new car with more advanced safety features might be worth the money. Spending some cash now
to avoid a catastrophic situaton later may well be worth it. 

Buying a car is an emotional decision for anyone, even someone who cares as little about the car she drives as my mom does. 
I wondered if:

1. Framing this problem in terms of expected value maximization would help clarify the right decision 
2. AI could help somehow 


I could have just asked ChatGPT for general advice, which it also often does well, especially for situations as common as
pondering a car purchase. I did not want to just ask ChatGPT to do the calculation for me - I trust it more to write code that does math
than to do math by itself. But one of the ways AI has served me best has been by turning somewhat vague specifications into software. 
So I asked ChatGPT to write a script that does the EV calculation for me. The result is in this repository. 

I had a lot of fun working with my mom to play with the numbers to see how they affected the final numbers. I was most surprised to find that

- The risk of a catastrophic accident factors fairly little to the end result, as long as the odds are low even without a new car's safety features
- How massive the depreciation cost of owning a new car is (I knew this already, but looking at the numbers made this feel more real)

Upon reflection, I think this script exposed two common cognitive biases affecting my and my mom's thinking:

- We both overindexed on the idea of a catastrophic accident 
- We underindexed on the depreciation cost, probably because it feels "invisible" 

I had a lot of fun with this, and I think it's a great example of a symbiotic interaction between humans, software, and AI. So I'm publishing it on GitHub, despite 
the code being 99% AI generated.
