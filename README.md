# Kong APIGW for pongpong

pongpong 을 구성하는 마이크로 서비스들의 API Gateway.

## docker-compose

`docker-compose`를 이용해서 api gateway 구동에 필요한 최소 서비스를 동작시킬 수 있다.
서비스 구성은 `docker-compose.yml`을 참고한다.

## kubernetes services

`./k8s` 디렉토리에 kubernetes 리소스가 정의되어 있음

서비스 구성 정보는 [k8s/](k8s/) 링크를 참고

### Steps

`kubectl`을 통해 서비스를 전개한다.

``` sh
# deploy kong-apigw
$ kubectl create -f k8s/kong-apigw

# deploy test-api
$ kubectl create -f k8s/default
```

`kubectl`로 서비스를 확인해 본다.

``` sh
# namespace: kong-apigw
$ kubectl get all -n kong-apigw
```

## kong-cli

kong admin api를 shell에서 조작할 수 있는 cli를 python invoke task로 제공한다.

설치 및 사용 방법은 [kong-cli/](kong-cli/) 링크를 참고

## tutorial

kong api gateway와 테스트 API를 kubernetes로 배포하고,

api gateway에 key-auth 플러그인을 셋업해서 인증 기능을 추가하는 튜토리얼 코드들이 들어 있음.

``` sh
$ tree tutorial
tutorial/
├── 00_deploy_apigw.sh
├── 01_deploy_testapi.sh
├── 02_register_testapi.sh
└── 03_set_key_auth_plugin.sh

# 하나씩 차례대로 실행해 본다.
$ ./tutorial/00_deploy_apigw.sh
$ ./tutorial/01_deploy_testapi.sh
$ ./tutorial/02_register_testapi.sh
$ ./tutorial/03_set_key_auth_plugin.sh
```

