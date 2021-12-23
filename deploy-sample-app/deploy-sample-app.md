# 部署样例Ngnix应用程序

### 简介

在创建了Kubernetes集群之后，您通常希望通过在集群中的节点上部署应用程序来进行尝试。在下面的步骤中，您将在3个pod上部署一个Nginx示例应用程序，并创建一个负载平衡器来在分配给该服务的节点之间分配服务流量。

### 先决条件

- 已经部署了kubernetes集群
- 成功访问kubernetes集群
- 配置了自定义的容器镜像

1. 在虚机终端上，编辑一个文件 `nginx_lb.yaml`.

   ```
   $ vi nginx_lb.yaml
   ```

2. 将下面的内容拷贝到文件中。Copy the following content into the file. It defines a deployment (`kind: Deployment`) for the `nginx` app, followed by a service definition with a type of LoadBalancer (`type: LoadBalancer`) that balances http traffic on port 80 for the `nginx` app. Save and exit the editor.它为nginx应用程序定义了一个部署（`kind:deployment`），并且定义了一个服务，该服务定义的类型为LoadBalancer（`type:LoadBalancer`），用于负载均衡nginx应用程序端口80上的http流量。保存并退出编辑器。

   ```
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-nginx
     labels:
       app: nginx
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
         - name: nginx
           image: nginx:1.7.9
           ports:
           - containerPort: 80
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: my-nginx-svc
     labels:
       app: nginx
   spec:
     type: LoadBalancer
     ports:
     - port: 80
     selector:
       app: nginx
   ```

3. 要在kubernetes集群中创建`nginx_lb.yaml`文件中定义的部署和服务，运行下面的命令：

   ```
   [opc@oke-bastion ~]$ kubectl apply -f nginx_lb.yaml
   deployment.apps/my-nginx created
   service/my-nginx-svc created
   [opc@oke-bastion ~]$ 
   ```

4. 负载均衡器从挂起状态到完全运行可能需要几分钟的时间。您可以通过输入`kubectl get all`查看集群的当前状态，其中的输出类似于以下内容：

   ```
   [opc@oke-bastion ~]$ kubectl get all
   NAME                            READY   STATUS    RESTARTS   AGE
   pod/my-nginx-5d59d67564-2tjbv   1/1     Running   0          95s
   pod/my-nginx-5d59d67564-mkldp   1/1     Running   0          95s
   pod/my-nginx-5d59d67564-z9btr   1/1     Running   0          95s
   
   NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
   service/kubernetes     ClusterIP      10.96.0.1       <none>          443/TCP        67m
   service/my-nginx-svc   LoadBalancer   10.96.165.165   146.56.187.83   80:32352/TCP   96s
   
   NAME                       READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/my-nginx   3/3     3            3           96s
   
   NAME                                  DESIRED   CURRENT   READY   AGE
   replicaset.apps/my-nginx-5d59d67564   3         3         3       96s
   [opc@oke-bastion ~]$ 
   ```

5. 输出显示`my-nginx`应用正在3个pod（pod/my-nginx）上运行，负载均衡器正在运行（service/my-nginx-svc），并且有一个外部IP（146.56.187.83），客户端可以使用该IP连接到部署在pod上的应用程序。

6. 打开浏览器, 输入 url `http://146.56.187.83`, 你可以看到Ngnix应用正在运行。

   ![image-20210727123753014](images/image-20210727123753014.png)

7. 如果是在公司内网或其他有限制的网络环境下，会出现下列错误信息，不允许http访问。![image-20210714153724741](images/image-20210714153724741.png)

   

8. 你可以用以下命令来删除Ngnix应用和负载均衡服务。

   ```
   [opc@oke-bastion ~]$ kubectl delete -f nginx_lb.yaml 
   deployment.apps "my-nginx" deleted
   service "my-nginx-svc" deleted
   [opc@oke-bastion ~]$
   ```

   

