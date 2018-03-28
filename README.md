# Kong APIGW for pongpong

pongpong 을 구성하는 마이크로 서비스들의 API Gateway.

## docker-compose

`docker-compose`를 이용해서 api gateway 구동에 필요한 최소 서비스를 동작시킬 수 있다.
서비스 구성은 `docker-compose.yml`을 참고한다.

## invoke tasks

kong admin api를 shell에서 조작할 수 있는 cli를 python invoke task로 제공한다.

### Installation

`pyenv-virtualenv`를 이용해서 invoke 환경을 구성한다.

``` sh
$ pyenv virtuaelnv 3.6.0 kong-cli
$ pyenv activate kong-cli
$ pip install -r requirements.txt
```

`inv -l` 명령어로 태스크를 확인

``` sh
(kong-cli) $ inv -l
Available tasks:

  consumer-create     https://getkong.org/docs/0.12.x/admin-api/#create-consumer
  consumer-delete     https://getkong.org/docs/0.12.x/admin-api/#delete-consumer
  consumer-list       https://getkong.org/docs/0.12.x/admin-api/#list-consumers
  consumer-retrieve   https://getkong.org/docs/0.12.x/admin-api/#retrieve-consumer
  rc                  shows invoke kong-cli run configuration

  :

# consumer-create 에 대한 도움말 보기
(kong-cli) $ inv consumer-create --help
Usage: inv[oke] [--core-opts] consumer-create [--options] [other tasks here ...]

Docstring:
  https://getkong.org/docs/0.12.x/admin-api/#create-consumer

  Options:
    -d STRING, --data=STRING   json string(e.g '{"username": "john.doe"}') or json payload file path (e.g @payload.json)

# consumer-create로 kong consumer 생성하기
(kong-cli) $ inv consumer-create -d '{"username": "testuser"}'

# 또는 payload.json를 링크
(kong-cli) $ inv consumer-create -d @payload.json
```

