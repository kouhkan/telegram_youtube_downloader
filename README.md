# Telegram YouTube Downloader

A telegram bot which can download youtube file(s) and upload it to user.


### TODO
- [x] Add user model
- [x] Add youtube model
- [x] Download file with *yt-dlp*
- [ ] Push download files into a queue (like celery)
- [ ] Upload files into *minio bucket* 
- [ ] Better management for which file is exists
- [ ] Add github action
- [ ] Dockerize project

### Run project
- Need to get a new telegram token as [botfather](https://telegram.me/BotFather)
- Create a postgres database
- Change .env-sample to .env file
- Replace your data into .env file
- Create a virtualenv
- Install requirements:

```pip install -r requirements.txt```

- Run main.py file