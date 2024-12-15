DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env

TG_ANIME_CONTAINER = tg-anime
TG_ANIME_FILE = docker-compose/tg-anime.yaml

ZROK_SHARE_CONTAINER = docker-compose-zrok-share-1
ZROK_SHARE_FILE = docker-compose/zrok-share.yaml

POSTGRES_CONTAINER  = postgres-db
POSTGRES_FILE = docker-compose/postgres.yaml

REDIS_CONTAINER = redis
REDIS_FILE = docker-compose/redis.yaml

.PHONY: tg-anime
tg-anime:
	${DC} -f ${TG_ANIME_FILE} ${ENV} up --build -d

.PHONY: tg-anime-down
tg-anime-down:
	${DC} -f ${TG_ANIME_FILE} down

.PHONY: tg-anime-logs
tg-anime-logs:
	${LOGS} ${TG_ANIME_CONTAINER} -f

.PHONY: tg-anime-shell
tg-anime-shell:
	${EXEC} ${TG_ANIME_CONTAINER} bash


.PHONY: zrok-share
zrok-share:
	${DC} -f ${ZROK_SHARE_FILE} ${ENV} up --detach

.PHONY: zrok-share-down
zrok-share-down:
	${DC} -f ${ZROK_SHARE_FILE} down --volumes

.PHONY: zrok-share-logs
zrok-share-logs:
	${LOGS} ${ZROK_SHARE_CONTAINER} -f


.PHONY: postgres
postgres:
	${DC} -f ${POSTGRES_FILE} up -d

.PHONY: postgres-down
postgres-down:
	${DC} -f ${POSTGRES_FILE} down

.PHONY: postgres-logs
postgres-logs:
	${LOGS} ${POSTGRES_CONTAINER} -f


.PHONY: redis
redis:
	${DC} -f ${REDIS_FILE} up -d

.PHONY: redis-down
redis-down:
	${DC} -f ${REDIS_FILE} down

.PHONY: redis-logs
redis-logs:
	${LOGS} ${REDIS_CONTAINER} -f
