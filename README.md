# Crypto Alarm: Concept and Demo

>This is not an official documentation, the original is in Chinese, this is just a rough translation

![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/Entity%20Relationship%20Diagram.jpeg)

## Introduction: what is Crypto Alarm and what is it used for
### What Crypto Alarm is NOT:

 1. It's NOT a technical analysis tool that will give you notifications on trading signals, in fact crypto market is such a nova and volatile market we don't even recommend day trading unless you are a veteran or have access to insider information. BUY and HODL on projects with potential usecases in the future is the way to go.
 2. It's NOT a professional financial adviser, you should still do your own research on individual projects you are planning to invest in. The metrics used in the algorithm is highly subjective.
 
> More over self education is The No.1 important thing in crypto investing, we recommend reading following 2 books before jump in:
> **Mastering Bitcoin: Unlocking Digital Cryptocurrencies** by Andreas Antonopoulos
>  **Cryptoassets: The Innovative Investor's Guide to Bitcoin and Beyond** by Chris Burniske and Jack Tatar

### What Crypto Alarm is:
1. It is an algorithm that will help you monitor critical metrics relating to the fundamental value of a crypto asset. So instead of checking on all hundreds of projects manually by yourself, the algorithm pre-select candidates with the most potential based on real time data for you, so you can use your limited time and focus on the right project and never let a good project pass you by.
2. It also monitor public sentiment through Google and Social Media to get a sense how "Hyped" a project is, so you don't rush in with the crowd at a bad timing chasing the hype. It's still a bad bet if you get in at the wrong time, even if it's a good project fundamentally.
3. It help you recognize a potential "Pump and Dump" by analyzing the data behind the marketing show

### How does it work under the hood
1. Collecting any data available in crypto space
2. Monitor big changes in metrics relating to the fundamental value of a cryptocurrency
3. Monitor public sentiment of each cryptocurrency
4. Giving each cryptocurrency a score on ***Fundamental Gains*** and ***Price and Hypes***.
5. List the top 10 undervalued and overvalued projects by **subtracting** the two scores above.

### What metrics are used
Again this is highly subjective and should be taken with a grain of salt. Bellow are the Metrics we have picked and the reason why:

#### Metrics 1: GitHub Activities
Despite the Stories and Marketing show circuling around the internet, Never forget this: Ultimately the ***CORE value*** of a cryptocurrency lies in its **Protocol** and various ***Applications*** surrounding it, in other words: it's a **Software**, more precisely **Open sourced Software**. And the core value of a software comes from the developers behind it. 
Luckily, because if the open sourced nature of cryptocurreny, we can easily monitor how the developing progress is going by simply checking it's github profile. We believe a Great Project will have a very **Active** GitHub profile, because:

 1. The team is really working on improving the protocal and developing various applications surrounding it so people can use it without dealing with the technical stuff.
 2. A promising project will attract more and more talented developers to contribute or fork the repositories, and usually those people have the Best understanding of cryptocurrency, following those people is like following world class hedge fund managers in a traditional investment market.
 3. A typical "Pump and Dump" show usually has no development backing their promise behind their marketing show, because they spend their resource on marketing and spamming instead of hire real talents.

So if a project has a big increase on their GitHub Activities, you should pay attention to it, or if you feel FOMO because some coin went up 5x in a month, check it's GH, if nothing is going on their, you know what's up.

#### Metrics 2: Adoption: how many people are using it
The best technology does not always win. Mass adoption is what ultimately decide how much your holding will be worth in 5 years. We monitor this by combining:
 1. Transactions
	 1. Daily Transactions
	 2. Daily Transaction value in USD
	 3. Daily Median transaction value in USD
 2. Active addresses
 3. Hash rate
 4. Wealth distribution

>A note on transaction volume data: depending on the protocol and degree of Anonymity, there can be different measurement for this metrics, we choose the one used by [coinmetrics.io](https://coinmetrics.io/), which is over estimate on it's absolute value but accurate on it's relative value, since we only care about the changes in most metrics, not the absolute value. Check this article from [coinmetrics.io](https://coinmetrics.io/) for more details: [On the difficulty of estimating on-chain transaction volume](https://coinmetrics.io/difficulty-estimating-chain-transaction-volume/)

#### Metrics 3: Hypes
You can still loose money on an awesome project if you jump in at a bad time, we monitor the sentiment and interest of the public as well:
 1. Searches on Google
 2. Searches on Baidu (Chinese Google)
 3. Tweets
 4. Headlines on Reddit News
 5. Sentiment based on the last two
#### Metrics4: Marketcap
This one seems simple but it's more than what you think, marketcap is not just marketcap, different coins have different proportions of reservation and circulating supply, we normalized this number so they are comparable
#### Other metrics:
Those are highly subjective, so we don't put too much weight on them:
 1. Decentralization level
 2. Road map progress
 3. ... ...

 
## Demo:
### Undervalued Top 10 
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/Top10undervalued.png)
### Hyper Top 10
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/Top10hype.png)
### Fundamental metrics correlation visualization, Bitcoin
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/correlationmatrix.png)
### Fundamental metrics correlation visualization, Ethererum
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/correlation%20matrxi%20eth.png)
### Market analysis visualization
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/marketanalysis.png)
### Fundamental analysis visualization
!Median transaction value is a good sign of a normal growth and an abnormal hype
![Alt Text](https://github.com/jorjiang/Crypto-Alarm/blob/master/image/fundamental%20analysis.png)
