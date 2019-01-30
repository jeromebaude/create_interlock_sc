#!/usr/bin/python
# This script creates a yaml to be used as a config for Interlock service
# Jerome Baude

import sys

def section(i):
    print('  [Extensions.sc-%d]' % i)
    print('    Image = "docker/ucp-interlock-extension:3.1.2"')
    print('    Args = []')
    print('    ServiceName = "ucp-interlock-extension-sc-%d"' % i)
    print('    Constraints = ["node.labels.com.docker.ucp.orchestrator.swarm==true", "node.platform.os==linux"]')
    print('    ProxyImage = "docker/ucp-interlock-proxy:3.1.2"')
    print('    ProxyArgs = []')
    print('    ProxyServiceName = "ucp-interlock-proxy-sc-%d"' % i)
    print('    ProxyConfigPath = "/etc/nginx/nginx.conf"')
    print('    ProxyReplicas = 2')
    print('    ProxyStopSignal = "SIGQUIT"')
    print('    ProxyStopGracePeriod = "5s"')
    print('    ProxyConstraints = ["node.labels.com.docker.ucp.orchestrator.swarm==true", "node.platform.os==linux", "node.labels.nodetype==loadbalancer"]')
    print('    ServiceCluster = "sc-%d"' % i)
    print('    PublishMode = "ingress"')
    print('    PublishedPort = %d' % (8000+i))
    print('    TargetPort = 80')
    print('    PublishedSSLPort = %d' % (8443+i))
    print('    TargetSSLPort = 443')
    print('    [Extensions.sc-%d.Config]' % i)
    print('     User = "nginx"')
    print('     PidPath = "/var/run/proxy.pid"')
    print('     WorkerProcesses = 1')
    print('     RlimitNoFile = 65535')
    print('     MaxConnections = 2048')
 
def main(argv):
    try:
        arg = sys.argv[1]
        nb = int (arg)
    except:
        print ('create_sc_config.py <nb_service_clusters>')
        sys.exit(2)
    
    print('ListenAddr = ":8080"')
    print('DockerURL = "unix:///var/run/docker.sock"')
    print('AllowInsecure = false')
    print('PollInterval = "3s"')
    print('')
    for i in range(nb):
        section (i+1)

if __name__ == "__main__":
   main(sys.argv[1:])   

