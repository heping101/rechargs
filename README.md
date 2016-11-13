runfast充值核心系统

* 前台地址：http://ap.runfast.cn/
* 管理地址：http://console.runfast.cn/

* 开发测试前端地址：http://ap.dev.runfast.cn/
* 开发测试管理后台：http://ap.dev.runfast.cn/


运行环境安装说明
-------------

##### 需安装以下相关软件：

* Python2 最新稳定版本
* Django
* python-memcached
* memcached --安装 python-memcached
* mysql-python
* redis

##### 注意：

开发测试环境请在 /etc/hosts 文件中添加以下设置：

```
127.0.0.1       mc.runfast.cn
```


代码更新发布说明
-------------

原则上必须将更新提交到 Git 后才可以部署到服务器。目前服务器分为产品环境和测试环境：

* 产品环境：ap.runfast.cn (http://ap.runfast.cn/)
* 测试环境：ap.dev.runfast.cn (https://ap.dev.runfast.cn/)

##### 代码更新部署步骤如下：

1、将更新代码部署到测试服务器：

    cd scripts/ && sh make_dist.sh && sh sync_demo.sh

2、测试没有问题后，将此更新发布到产品服务器：

    cd scripts/ && sh make_dist.sh && sh sync_dist.sh

##### 注意：

make_dist.sh 脚本接受第一个参数作为同步指定的版本号，比如要更新到 370ec42fa33eec8d448a15bb66e38d03ce71ab10 这个 commit id 对应的版本：

    cd scripts/ && sh make_dist.sh 370ec42fa33eec8d448a15bb66e38d03ce71ab10 && sh sync_dev.sh

