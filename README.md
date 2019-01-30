# create_interlock_sc

This script aims at generating docker config for ucp-interlock in a service cluster mode.

(Details can be found here: https://docs.docker.com/ee/ucp/interlock/usage/service-clusters/)

How to create your ucp-interlock config:
```
python create_sc_config.py <nb_service_clusters> | docker config create com.docker.ucp.interlock.conf-1 -
```

Example:
```
python create_sc_config.py 1
```
ListenAddr = ":8080"
DockerURL = "unix:///var/run/docker.sock"
AllowInsecure = false
PollInterval = "3s"

  [Extensions.sc-1]
    Image = "docker/ucp-interlock-extension:3.1.2"
    Args = []
    ServiceName = "ucp-interlock-extension-sc-1"
    Constraints = ["node.labels.com.docker.ucp.orchestrator.swarm==true", "node.platform.os==linux"]
    ProxyImage = "docker/ucp-interlock-proxy:3.1.2"
    ProxyArgs = []
    ProxyServiceName = "ucp-interlock-proxy-sc-1"
    ProxyConfigPath = "/etc/nginx/nginx.conf"
    ProxyReplicas = 2
    ProxyStopSignal = "SIGQUIT"
    ProxyStopGracePeriod = "5s"
    ProxyConstraints = ["node.labels.com.docker.ucp.orchestrator.swarm==true", "node.platform.os==linux", "node.labels.nodetype==loadbalancer"]
    ServiceCluster = "sc-1"
    PublishMode = "ingress"
    PublishedPort = 8001
    TargetPort = 80
    PublishedSSLPort = 8444
    TargetSSLPort = 443
    [Extensions.sc-1.Config]
     User = "nginx"
     PidPath = "/var/run/proxy.pid"
     WorkerProcesses = 1
     RlimitNoFile = 65535
     MaxConnections = 2048
