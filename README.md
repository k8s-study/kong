# Kong APIGW for pongpong

pongpong 을 구성하는 마이크로 서비스들의 API Gateway.

## docker-compose

`docker-compose`를 이용해서 api gateway 구동에 필요한 최소 서비스를 동작시킬 수 있다.
서비스 구성은 `docker-compose.yml`을 참고한다.

## kubernetes services

`./k8s` 디렉토리에 kubernetes 리소스가 정의되어 있음

### structure

``` txt
+=< svc_kong-database.yml >==+           +< job_kong-migration.yml >+
|                            |           |                          |
|    +------------------+    |           |  +-------------------+   |
|    | po/kong-database |    |           |  | po/kong-migration |   |
|    +------------------+    |           |  +-------------------+   |
|             |              |           |            |             |
|             | :5432        |           |            |             |
|    +--------V----------+   |           |  +--------------------+  |
|    | svc/kong-database | <--- migrate --- | job/kong-migration |  |
|    +--------+----------+   |           |  +--------------------+  |
|             |              |           |                          |
+=============|==============+           +==========================+
              | ClusterIP:5432
              |
            +-----------------+
            |                 |
+========< deploy_kong-apigw.yml >============+
|           |                 |               |
|  +-----------------+ +-----------------+    |
|  | po/kong-apigw-1 | | po/kong-apigw-2 | .. |
|  +-----------------+ +-----------------+    |
|          |                  |               |
|          +------------------+               |
|            |                                |
+============|================================+
             | ContainerPort :8000,  :8001,  :8443,  :8444
             | ServicePort   :10080, :10082, :10443, :10444
             |
+=< svc_kong-apigw.yml >=+   +=< ingress_kong-apigw.yml >=+
|            |           |   |                            |
|  +----------------+    |   |   +--------------------+   |
|  | svc/kong-apigw |------------| ingress-kong-apigw |   |
|  +----------------+    |   |   +--------------------+   |
|                        |   |            |               |
+========================+   +============|===============+
                                          | 10080 -> apigw.pong.com:80
                                          | 10081 -> apigw-admin.pong.com:80
                                          |
    ===================================== | ========
                                          V
```

### Steps

`kubectl`을 통해 서비스를 전개한다.

``` sh
$ kubectl create -f k8s/
```

`kubectl`로 서비스를 확인해 본다.

``` sh
$ kubectl get all
NAME                DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/kong-apigw   2         2         2            2           23m

NAME                      DESIRED   CURRENT   READY     AGE
rs/kong-apigw-6b7d95b77   2         2         2         23m

NAME                DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/kong-apigw   2         2         2            2           23m

NAME                      DESIRED   CURRENT   READY     AGE
rs/kong-apigw-6b7d95b77   2         2         2         23m

NAME                  DESIRED   SUCCESSFUL   AGE
jobs/kong-migration   1         1            23m

NAME                            READY     STATUS    RESTARTS   AGE
po/kong-apigw-6b7d95b77-db75h   1/1       Running   2          23m
po/kong-apigw-6b7d95b77-wc6hd   1/1       Running   2          23m
po/kong-database                1/1       Running   0          23m

NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                           AGE
svc/kong-apigw      NodePort    10.102.85.184    <none>        10080:30792/TCP,10443:31423/TCP,10081:30411/TCP,10444:32227/TCP   23m
svc/kong-database   ClusterIP   10.110.118.134   <none>        5432/TCP                                                          23m
svc/kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP                                                           5d
```

`minikube`로 클러스터 외부로 노출된 서비스를 확인해 본다.

``` sh
$ minikube service list
|-------------|----------------------|--------------------------------|
|  NAMESPACE  |         NAME         |              URL               |
|-------------|----------------------|--------------------------------|
| default     | kong-apigw           | http://192.168.99.100:30792    |
|             |                      | http://192.168.99.100:31423    |
|             |                      | http://192.168.99.100:30411    |
|             |                      | http://192.168.99.100:32227    |
| default     | kong-database        | No node port                   |
| default     | kubernetes           | No node port                   |
| kube-system | kube-dns             | No node port                   |
| kube-system | kubernetes-dashboard | http://192.168.99.100:30000    |
|-------------|----------------------|--------------------------------|
```

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

