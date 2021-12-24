# 部署样例应用程序

## 简介

在创建了Kubernetes集群之后，您可以尝试在集群中的节点上部署应用程序。在下面的步骤中，您将把之前创建的容器镜像部署在集群中，相同的应用程序运行在3个pod中，由一个负载平衡器来在分配给该服务的节点之间分配服务流量。

### 先决条件

- 已经部署了kubernetes集群
- 成功访问kubernetes集群
- 配置了自定义的容器镜像

## Task 1：部署样例应用程序

1. 在虚机终端上，编辑一个文件 `myfirstapp_lb.yaml`。将下面的内容拷贝到文件中。

   - `kind: Deployment`: 为应用程序定义了一个部署
   - `replicas: 3`: 运行3个pods
   - `image: <your_name>/myfirstapp:1.0`: 要运行的容器镜像，请使用你在docker hub中注册的用户名，如果本地镜像不存在，则从远程资料库中获取。 
   - `type: LoadBalancer`: 定义了一个类型为LoadBalancer的服务, 用于负载均衡到后端的应用程序。

   ```
   <copy>
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: myapp
     labels:
       app: myapp
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: myapp
     template:
       metadata:
         labels:
           app: myapp
       spec:
         containers:
         - name: myapp
           image: minqiao/myfirstapp:1.0
           ports:
           - containerPort: 5000
             protocol: TCP
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: myapp-svc
     labels:
       app: myapp
   spec:
     type: LoadBalancer
     ports:
     - port: 80
       protocol: TCP
       targetPort: 5000
     selector:
       app: myapp
   </copy>
   ```

3. 要在kubernetes集群中创建`myfirstapp_lb.yaml`文件中定义的部署和服务，运行下面的命令：

   ```
   [opc@oke-bastion ~]$ kubectl apply -f myfirstapp_lb.yaml
   deployment.apps/my-nginx created
   service/my-nginx-svc created
   [opc@oke-bastion ~]$ 
   ```

3. 负载均衡器从挂起状态到完全运行可能需要几分钟的时间。您可以通过输入`kubectl get pod,svc`查看集群pod和服务的运行状态，其中的输出类似于以下内容：

   ```
   $ kubectl get pod,svc
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
   
   ```

   - 输出显示`myapp`应用正在3个pod（pod/myapp）上运行，负载均衡器正在运行（service/myapp-svc），并且有一个外部IP（146.56.187.83），客户端可以使用该IP连接到部署在pod上的应用程序。

6. 打开浏览器, 输入 url `http://<your_lb_publicIP>`, 你可以看到应用运行正常。

   ![image-20211224151052651](images/image-20211224151052651.png)

7. 如果是在公司内网或其他有限制的网络环境下，会出现下列错误信息，不允许http访问。可以采用其他网络进行访问。![image-20210714153724741](images/image-20210714153724741.png)

   

8. 用以下命令来删除部署的应用和负载均衡服务。

   ```
   $ kubectl delete -f myfirstapp_lb.yaml 
   deployment.apps "myapp" deleted
   service "myapp-svc" deleted
   $
   ```

   

