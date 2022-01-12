# 创建Kubernetes集群 

## 简介

通过本练习，你将学习到如何在OCI上创建 Kubernetes集群。OCI中由Kubernetes 集群控制平台来实现 Kubernetes 的核心功能，集群控制平台完全由 Oracle 管理，而且是免费的。OCI仅收取计算和存储的费用。



### 先决条件

- 你需要OCI租户账号，并且Container Engine for Kubernetes可用.
- 你的租户必须有足够的不同资源的配额，如：计算资源，块存储资源，Load Balancer资源，等等。
- 要创建或管理k8s集群，你必须属于具有合适的OKE权限的组
- 在 root compartment中设置策略（ policy）：  ```allow service OKE to manage all-resources in tenancy```.
- 一组SSH键用来访问集群中的工作节点和堡垒机

## Task 1：利用缺省设置快速创建Kubernetes集群

1. 登录到**OCI控制台**，打开**导航菜单**，选择**开发人员服务**，在**容器和构件**下点击**Kubernetes集群（OKE）**。

   ![image-20210714201001944](images/image-20210714201001944.png)

2. 选择合适的**区域（Region）**和**区间（Compartment）**，点击**创建集群**。

   ![image-20211223142428329](images/image-20211223142428329.png)

3. 在**创建集群**对话框里，选择**快速创建**，点击**启动工作流**。

   ![image-20210714201725763](images/image-20210714201725763.png)

4. 在**创建集群**页面，按以下内容选择或输入：

   - **名称:** 任意唯一的合法名称，如：mycluster01
   - **区间:** 选择你将要部署Kubernetes集群的区间。
   - **Kubernetes 版本:** 接受缺省值（最新版本）
   - **Kubernetes API端点:** 接受缺省选项，公共端点。
   - **Kubernetes Worker节点:** 接受缺省选项，专用Worker。

   ![image-20211223142756888](images/image-20211223142756888.png)

   - **配置:** 接受缺省配置，VM.Standard.E3.Flex, 1 OCPU, 16G内存

   - **节点数量:** 接受缺省值: 3

       ![image-20211223142841528](images/image-20211223142841528.png)

       

   

6. 点击**下一步**复查要创建的集群的详细信息。

   ![image-20211223143056705](images/image-20211223143056705.png)

7. 点击**创建集群**，开始创建新的网络资源和新的集群。

   ![image-20210715101545675](images/image-20210715101545675.png)

8. 点击**关闭**，来到集群详细信息页面。 可以看到当前集群正在创建中。

   ![image-20211223143402275](images/image-20211223143402275.png)

9. 等待10分钟左右，集群状态变成活动状态。

   ![image-20211223144117338](images/image-20211223144117338.png)

9. 在**资源**下选择**节点池**，可以看到已经有一个节点池创建，名字为：pool1。点击pool1，进入节点池详细信息页面。

  ![image-20211223144229110](images/image-20211223144229110.png)

  

12. 在**资源**下选择**节点**，可以看到当前有3个节点还在不可用状态。

    ![image-20211223144401164](images/image-20211223144401164.png)

13. 几分钟后，3个节点都变成**就绪**状态，集群创建成功。

    ![image-20211223144922244](images/image-20211223144922244.png)



## Task 2：查看Kubenetes集群的信息

1. 打开**导航菜单**，选择**网络**，点击**虚拟云网络**。

   ![image-20210715103605652](images/image-20210715103605652.png)

2. 可以看到新创建的VCN，名称为：`oke-vcn-mycluster01-***`。点击该名称链接。

   ![image-20211223145043087](images/image-20211223145043087.png)

3. 在虚拟网络详细信息页面，可以看到三个子网，分别对应Load Balancer，Worker节点，以及Kubernetes API Endpoint。点击`oke-k8sApiEndpoint-quick-mycluster01-*`子网。

   ![image-20211223145158203](images/image-20211223145158203.png)

4. 点击对应的安全列表链接。

   ![image-20211223150004542](images/image-20211223150004542.png)

5. 查看缺省配置好的入站出站规则。

   ![image-20211223150111823](images/image-20211223150111823.png)

   

6. 打开**导航菜单**，选择**计算**，点击**实例**。

   ![image-20210715104337910](images/image-20210715104337910.png)

7. 可以看到新创建的3个节点实例。

   ![image-20211223150241534](images/image-20211223150241534.png)

   

   Kubernetes集群已经创建完成，现在你可以开始下一个实验。

   

