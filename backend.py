import requests,json


pid = "16265164.4065424769106"

data = {
    "SKU": pid,
    "cartPosition": None,
    "recaptchaResponse": False,
    "quantityToAdd": 1,
    "customisations": []
}

cartheaders = {
        'Host':'m.jdsports.co.uk',
        'content-type':'application/json',
        'accept':'*/*',
        'Accept':'application/json',
        'accept-language':'en-US,en;q=0.9',
        'User-Agent':'Amazon CloudFront',
        'x-newrelic-id':'1',
        'Akamai-Bot':'Customer-Categorized Bot (Mission Lab IP):monitor:ML BM Bypass',
        'Akamai-Origin-Hop':'2',
        'Cache-Control':'no-cache:max-age=0',
        'Cloudfront-Forwarded-Proto':'https',
        'Cloudfront-Is-Desktop-Viewer':'false',
        'Cloudfront-Is-Mobile-Viewer':'true',
        'Cloudfront-Is-Smarttv-Viewer':'false',
        'Cloudfront-Is-Tablet-Viewer':'false',
        'Cloudfront-Viewer-Country':'UK',
        'Pragma':'no-cache',
        'True-Client-Ip':'34.253.69.187',
        'Via':'1.1 v1-akamaitech.net(ghost) (AkamaiGHost):1.1 akamai.net(ghost) (AkamaiGHost):1.1 16490f661d04b5f69e5cda7988ce930b.cloudfront.net (CloudFront)',
        'X-Akamai-Config-Log-Detail':'true',
        'X-Amz-Cf-Id':'eFi-0J9EgK-6ohJnY204KzbEimyOavyPCeK6wSC8G2P8DpXCBeL9FQ==',
        'X-Amzn-Trace-Id':'Root=1-5f561d4e-6d8cde9cc5e61158141bb5c4',
        'X-Forwarded-For':'34.253.69.187:184.28.198.53:23.62.238.237',
        'X-Forwarded-Port':'443',
        'X-Forwarded-Proto':'https',
        'X-Varnish':'289801518' 
    }

url = f"https://config.jdmesh.co/cart/{pid}"

r = requests.post(url, json=data, headers=cartheaders)

print(r.json())
