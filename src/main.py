from fastapi import FastAPI
from src import get_twitter_data
from src import get_processed_data
import extract_tweet_sentiment as es
import asyncio
import uuid

app = FastAPI()

@app.get("/")
def read_root():
    return ("Welcome to Crypto Sentiment Analytics")

@app.get("/getTweets/{twitter_handle}")
async def get_tweets(twitter_handle: str):
    count = get_twitter_data.get_all_user_tweets(twitter_handle)
    return (str(count) + " Tweets fetched successfully")
    #http://127.0.0.1:8004/getTweets/OneDevloperArmy


@app.get("/analyseTweetSentiments/{twitter_handle}")
async def analyse_tweet_sentiments(twitter_handle: str):
    return es.extract_sentiment(twitter_handle+'.json')
    #http://127.0.0.1:8004/analyseTweetSentiments/OneDevloperArmy


@app.get("/getProcessedSentiment/{twitter_handle}")
async def get_processed_sentiment(twitter_handle: str):
    return get_processed_data.get_processed_sentiment(twitter_handle)
    #http://127.0.0.1:8004/getProcessedSentiment/OneDevloperArmy


'''
#https://stackoverflow.com/questions/64901945/how-to-send-a-progress-of-operation-in-a-fastapi-app

context = {'jobs': {}}

async def do_work(job_key, files=None):
    iter_over = files if files else range(100)
    for file, file_number in enumerate(iter_over):
        jobs = context['jobs']
        job_info = jobs[job_key]
        job_info['iteration'] = file_number
        job_info['status'] = 'inprogress'
        await asyncio.sleep(1)
    pending_jobs[job_key]['status'] = 'done'


@app.post('/work/test')
async def testing(files: List[UploadFile]):
    identifier = str(uuid.uuid4())
    context[jobs][identifier] = {}
    asyncio.run_coroutine_threadsafe(do_work(identifier, files), loop=asyncio.get_running_loop())
    return {"identifier": identifier}


@app.get('/')
async def get_testing():
    identifier = str(uuid.uuid4())
    context['jobs'][identifier] = {}
    asyncio.run_coroutine_threadsafe(do_work(identifier), loop=asyncio.get_running_loop())
    return {"identifier": identifier}

@app.get('/status')
def status():
    return {
        'all': list(context['jobs'].values()),
    }


@app.get('/status/{identifier}')
async def status(identifier):
    return {
        "status": context['jobs'].get(identifier, 'job with that identifier is undefined'),
    }
'''