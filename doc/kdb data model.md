## 数据模型

### 用户系统

* T_USER

  描述: 用户
  列 | 类型 | 取值范围 | 默认值 | 非空 | 描述
  -|-|-|-|-|-
  id||||Y|用户id
  name||||Y|用户名称
  passwd||||Y|密码
  role|||||角色
  desc|||||

* T_ROLE

  描述: 角色
  列 | 类型 | 取值范围 | 默认值 | 非空 | 描述
  -|-|-|-|-|-
  id|||||角色id
  name|||||角色名称
  op|||||可完成的操作
  desc|||||

* T_OPERATION

  描述: 操作
  列 | 类型 | 取值范围 | 默认值 | 非空 | 描述
  -|-|-|-|-|-
  id|||||操作id
  name|||||操作名称
  desc|||||

* T_ACTIVITY

  描述: 活动, 记录用户行为, 如登录, 登出
  列 | 类型 | 取值范围 | 默认值 | 非空 | 描述
  -|-|-|-|-|-
  user_id|||||用户
  activity|||||活动, 如登录, 查询
  detail|||||活动详细描述
  datetime|||||活动时间
  desc|||||

> 一期只实现用户表, 不分角色, 无操作权限管理, 无活动记录

### 业务系统

* T_SHOP
  
  描述: 预先导入的数据, 记录店铺信息
  列 | 类型 | 取值范围 | 默认值 | 非空 | 描述
  -|-|-|-|-|-
  id|||||店铺id
  name|||||店铺名称
  location|||||地点

  > 更多属性可在后期按需添加, 可新建一个表, 记录好评信息等

* T_BOOK
  
  描述: 记录图书信息
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  id|||||ISBN
  name|||||书名
  price|||||定价
  press|||||出版社
  author|||||作者

  > 更多属性可在后期按需添加, 作者可以单独出来一个表
  
* T_CATEGORY
  
  描述: 预先导入的数据, 记录分类信息
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  id|||||类别id
  name|||||类别名称
  
* T_PRESS
  
  描述: 记录出版社信息
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  id|||||出版社id
  name|||||出版社名称

* T_AUTHOR
  
  描述: 记录作者信息
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  id|||||作者id
  name|||||作者姓名

* T_DATATYPE
  
  描述: 字典表, 售价、折扣、销量，流量，评论量，直通车投入
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  key|||||数据项
  type|||||数据项类别
  desc|||||
  
* T_BUSINESS
  
  描述: 业务信息和业务需求的数据类型, 单品销售情况查询, 竞品情况比较, 某类目特殊表现监控
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  business_id|||||功能id
  business|||||功能名称
  data_type|||||所需数据类型
  
* T_DATA
  
  描述: 按日期记录各店铺中各图书的各数据项的值
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  shop_id|||||店铺id
  book_id|||||图书id
  key|||||数据类型
  value|||||值
  date|||||日期
  
* T_TEMPLATE
  描述: 用户保存的查询模板或者查询历史记录
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  user_id|||||用户
  business_id|||||业务/功能
  vale|||||内容
  
* T_FUNCTION
  描述: 数据项值异常定义
  列 | 类型 | 取值范围 | 默认值 | 空 | 描述
  -|-|-|-|-|-
  datatype_id|||||数据项
  operator|||||操作符
  value|||||值
  duration|||||周期
  type|||||类型, 如百分比, 绝对值等

  > 公式一期定义为 `XXX >/</= value` 的格式, 后期实现更强大的自定义

### 其他

* T_FAVOR
  描述: 自选, 重点关注图书或店铺

  > 暂时不展开, 一期不实现