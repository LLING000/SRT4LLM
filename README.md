# SRT4LLM
我们提出了一套针对空间地理问题的大语言模型测试标准SRT4LLM，分别从空间场景中图形对象类型、空间关系和Prompt策略三个维度研究构建测试体系，最终形成三种空间对象类型、三种空间关系和三种提示工程和标准测试流程的测试标准。

## SRT4LLM框架
为系统评估大语言模型在空间地理问题上的认知能力，本研究提出了面向大模型的空间认知测试标准框架SRT4LLM。SRT4LLM架构包含三个递进的逻辑层次，一是三种基础空间关系；二是在此基础上的逐渐复杂的空间对象类型及其组合关系；三是从简单提示到引导性提示和示例性提示的渐次复杂的提示工程。

![image](https://github.com/user-attachments/assets/6cfc0fa2-3b8d-4b04-a5ee-ba4e3374a4f9)

## 标准化提问模板
模板包括三个关键组成部分构成：任务指令、空间关系的定义（拓扑关系、方位关系和距离关系）以及被测对象的位置坐标。
考虑到测试中涉及国内外多种大模型的对比分析，为确保实验的一致性和可比性，本研究统一采用采用英文作为标准输入语言。

## 测试空间场景
### 简单空间场景

拓扑关系：

![scene-topo](https://github.com/user-attachments/assets/d6a087d3-83ef-4b39-99dc-57a1082b3b80)


方位关系：

![scene-dir](https://github.com/user-attachments/assets/7bb0cf2c-0bc4-4d7d-ac6f-3cd142f67dda)


距离关系：

![scene-dis](https://github.com/user-attachments/assets/492d738c-d113-4c6b-8efb-aa707bb98bb5)


### 复杂空间场景

![data_complex](https://github.com/user-attachments/assets/1fed23d5-244a-4139-84e8-0726e785e37d)

## Prompt模板
SRT4LLM 提出了三种提示工程方法：简单提示（Simple Prompt, SP）、引导提示（Guiding Prompt, GP）和示例提示（Example Prompt, EP）。

### 使用
文件包含使用简单空间场景和复杂空间场景对三种空间关系提问的prompt模板，将大模型连接即可使用。
