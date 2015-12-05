# WatsonDisasterApp

## Execution

```
python run.py
```

* Read tweets filtered by `app/apis/twitter/SEARCH_KEY_WORD`
* Add priority by Watson
* Register record to kintone

## Setting

create `environment.yaml` on your repository root.

```
kintone:
    domain: your kintone domain
    app_id: application id
    api_token: application's api token
watson:
    id: your_watson_id
    password: your_watson_password
	classifier:
        classifier_category: your_category_classifier_id 
twitter:
    consumer_key: your_consumer_key
    consumer_secret: your_consumer_secret
    token: your_token
    token_secret: your_secret
```
