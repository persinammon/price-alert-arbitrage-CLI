# Price Alert

## Motivation

One of my hobbies is buying and selling makeup. Makeup has a heavy price mark up, and
the beauty industry pushes layers of products on top of that. A full set 
of makeup can easily cost $200+.

I wrote a Python program to create a scraper instance based on a given configuration (skincare and makeup in my case).

Daily job:
- scrape buy/sell sites and send message to SNS topic
- on-publish insert record into database, perform analytics, and email if good opportunity to buy arises

I am running the program on a HTTP server which will allow configuration requests from other people to
be included as well, eventually.

## Stack and Third Party Software

- Python 3.10
- Beautiful Soup 4
- Apache HTTP Web Server
- Amazon AWS Free Tier
    - EC2 t2.micro instance to host scripts and run computation
    - EBS volume to persist data
    - SNS topic for second program to save to a local database
- PostgreSQL
- CircleCI pipeline


### Set Up Your Own Alert

Right now I've kept the server open access to submit own price alert and email through HTTP.
Obviously, there are security hazards I will think through after the initial example works/is optimized.

```
curl -H "Content-Type: application/json" \
  --request POST \
  --data '{"buy_sites": ["url", "url", ..], \
    "brands": ["string", "string", ..], \
    "product_names" : [], \
    "sell_sites": []}  \
  {CURRENT_EC2_INSTANCE_IP}

```

##### Example makeup stack, for those curious:

Eyes
- mascara - $10-25
- eyeliner, and/or liquid and smokey eye - $20
- eyeshadow palette - $50+
Face
- foundation $25
- concealer $10
- primer $10
- setting spray $10
Lips
- lipstick $10-20
- lipliner $8
Equipment
- brushes $20

Multiple products in skincare is also a trend.