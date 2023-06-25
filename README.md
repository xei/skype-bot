# Skype Bot Service

## Health Check
```bash
curl --location 'https://ml.hosseinkhani.me/skype-bot/healthz'
```

## Send Message to a contact (skype_name)
```bash
curl -X 'POST' \
  'https://ml.hosseinkhani.me/skype-bot/send-msg/contact/contact_name' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "msg": "hi!"
}'
```
## Send message to a group (chat_id)
```bash
curl -X 'POST' \
  'https://ml.hosseinkhani.me/skype-bot/send-msg/chat/group_id' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "msg": "hi!"
}'
```

## API Document
+ https://ml.hosseinkhani.me/skype-bot/docs


## Run on local system without Docker
```bash
git clone https://github.com/xei/skype-bot.git
cd skype-bot
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
PYTHONPATH=PATH/TO/PROJ/app uvicorn main:app --reload
```

## Run on local system with Docker
```
docker pull $CONTAINER_REGISTRY_PATH/skype-bot:latest
docker run $CONTAINER_REGISTRY_PATH/skype-bot:latest
```

## Deploy new changes (It is automated in Gitlab CI)
```bash
docker pull $CONTAINER_REGISTRY_PATH/skype-bot:latest || true
docker build --cache-from $CONTAINER_REGISTRY_PATH/skype-bot:latest -f Dockerfile -t $CONTAINER_REGISTRY_PATH/skype-bot:latest .
docker push $CONTAINER_REGISTRY_PATH/skype-bot:latest
docker stack deploy -c docker-compose.yml --with-registry-auth skype-bot
```
