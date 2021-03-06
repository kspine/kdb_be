## 业务流程
### 数据产生
* 系统外数据

  爬虫系统爬取开放数据

  爬虫系统爬取账号数据

  按日期, 分店铺, 分图书保存各数据项

* 系统产生数据
  
  用户信息, 账号, 密码

  活动信息, 即用户活动记录

  系统设置, 如告警设置

  用户保存信息, 如模板, 历史记录, 公式等

### 数据使用

* 登录

* 各业务查询
  
  1. 单品销售情况查询

     in: ISBN 日期
     > 日期, 具体某一天, 最近一周, 最近一月等

     out:  
     店铺|售价|折扣|销量|流量|评论量|直通车投入
     -|-|-|-|-|-|-
     店铺A|25|9.0|1000|20|300|10000
     店铺B|25|9.0|1000|20|300|10000
     店铺C|25|9.0|1000|20|300|10000
  
     > 可以根据 **售价|折扣|销量|流量|评论量|直通车投入** 进行排序
     
     > 数据量估算, N个店铺, 就是N条数据, 多天的数据会被聚合后返回前端

  2. 竞品情况比较
     
     in: N*店铺_ISBN + 数据项 + 周期
     > N <= 9, 周期 <= 365

     out: N(9)宫格
     
     ||||
     -|-|-|-
     A | B | C
     D | E | F
     G | H | I

     > 每个宫格内容为某一同一 **数据项** 在指定 **周期** 的曲线图

     > 宫格数的限制, 后期开发可以去掉
  
  3. 某类目特殊表现监
     in: 数据项
     out: 异常结果

     > 注意, 此功能实现只存储公式, 不存储结果, 请求时根据最新公式现取数据现计算, 再返回

     > 后期开发可以支持结果快照功能