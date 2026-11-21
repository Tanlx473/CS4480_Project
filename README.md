# FunnelLag

**CS4480 Data Intensive Computing · 电商点击、支付与退款的延迟分析**

用户点击商品后多久会支付？一笔支付发生后，要等多久才能观察到退款？FunnelLag 计划用 PySpark 处理淘宝 CASCADE 样本，研究两段等待时间，并测量 Spark 在不同配置下完成同一统计任务所需的时间。

当前阶段为仓库初始化。开发范围、分工与验收标准见[中文开发手册](docs/CASCADE_中文开发文档.pdf)。手册中的旧项目名称为 CASCADE Analytics，本仓库使用 FunnelLag，对应的 Python 包名为 `funnellag`。

## 分析目标

| 模块 | 计划回答的问题 |
| --- | --- |
| 事件延迟 | 已观察到支付的有效点击中，首次支付延迟的中位数和 P90 是多少？对于能确认支付与退款对应关系的样本，首次退款延迟如何分布？ |
| 观察窗口 | 固定一组有完整 72 小时随访的样本，在点击或支付后 1、24、72 小时内分别能看到多少目标事件？计算前须确认随访截止时间。 |
| Spark 性能 | 在同一台机器上分别改变核数、输入规模、分区数和输入格式（原始文本或 Parquet），查询耗时和吞吐量如何变化？ |

统计结论限定于数据样本及各指标的有效子集。计划由 PySpark 离线生成统计表，Jupyter Notebook 解释结果，Streamlit 读取预计算结果供交互查看。

## 数据与本地准备

数据来源为 [alimamaTech/CASCADE](https://huggingface.co/datasets/alimamaTech/CASCADE)。本次快照包含 25 个按日命名的文本文件，文件名从 `data_20250501.txt` 到 `data_20250525.txt`，共 21,408,886,953 字节。文件名中的日期用于定位输入，各事件的观察期限需要另行验证。

从仓库根目录工作。已有快照的组员可直接检查 `data/raw/data/data_*.txt`。新克隆仓库的组员可用 Hugging Face CLI 恢复同一版本的输入文件：

```sh
hf download alimamaTech/CASCADE --repo-type dataset \
  --revision dcca178668b60d937f66535a60a0a92c74c1dfde \
  --include 'data/data_*.txt' --local-dir data/raw
```

[原始数据清单](data/manifests/raw_manifest.json)记录版本、仓库相对路径、文件大小和 SHA-256，供组员核对输入。Git 保存清单，原始快照只在本地保存。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `src/funnellag/` | Python 包，后续实现解析、质量检查、统计和性能实验 |
| `configs/` | 分析口径与 Spark 实验配置 |
| `data/raw/` | 原始下载快照，每日文件位于其下的 `data/` |
| `data/manifests/` | 可版本控制的输入清单 |
| `data/processed/`、`data/rejected/` | 处理后的 Parquet、解析失败的记录及原因 |
| `notebooks/`、`dashboard/` | Jupyter 分析笔记、Streamlit 展示入口 |
| `tests/fixtures/` | 测试使用的小型样例，测试代码放在 `tests/` |
| `results/`、`logs/` | 按运行编号保存统计表、图表、性能数据及日志 |
| `docs/`、`report/` | 团队开发文档、课程报告 |

## 环境与运行

开发手册建议的基线为 Python 3.11、Java 17 和 PySpark 3.5.7。依赖安装、小样本运行、完整分析与 Dashboard 启动命令将在相应入口通过验证后补充。

## 结果

待首次可复现运行后补充样本覆盖范围、延迟分布、观察窗口统计和四组性能实验结果。

## 团队分工

| 角色 | 负责内容 |
| --- | --- |
| 成员 A | 数据来源、字段核对、解析和 Parquet 流水线 |
| 成员 B | 统计口径、延迟与窗口分析、图表和 Notebook |
| 成员 C | Spark 性能实验、Streamlit、集成和复现 |

## 许可

项目代码许可待团队确定。原始数据的使用条款见[数据集主页](https://huggingface.co/datasets/alimamaTech/CASCADE)。
