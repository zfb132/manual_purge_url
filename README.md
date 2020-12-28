# manual_purge_url
腾讯云函数：通过API触发，对CDN的所有URL进行刷新

## 功能
* 根据网址，对`https://{}/sitemap.xml`的链接进行刷新
* 根据`urls.txt`，对其中的所有链接进行刷新
* 在腾讯云函数的触发条件，选择API网关触发

API网关触发，相关参数设置如下  
选项 | 值 |  
:--:|:--:|  
API网关触发器所属版本 | $LATEST |  
API服务名 | update-cdn-purge_url |  
serviceId | service-abcdefgh |  
apiId | api-78abcdef |  
请求方法 | POST |  
发布环境 | 发布 |  
鉴权方式 | 免鉴权 |  
启用集成响应 | 未启用 |  
支持CORS | 否 |  
后端超时 | 15s |  
访问路径 | [发布版网关链接](https://service-abcdefgh-6688661199.sh.apigw.tencentcs.com/release/my-scf-name) |  

## 使用方法
* 修改`config.example.py`的各个变量为自己需要的值
* 修改`config.example.py`名称为`config.py`
* 按需修改`urls.txt`的链接
* 安装依赖：在仓库主目录执行`pip3 install -r requirements.txt -t .`
* 上传文件夹：腾讯云函数，提交方式，选择`本地上传文件夹`，选择该仓库的文件夹即可（保证该文件夹根目录应包含`index.main_handler`方法）

## 触发方法
可在终端使用如下命令触发云函数  
`curl -X POST https://service-abcdefgh-6688661199.sh.apigw.tencentcs.com/release/my-scf-name`
