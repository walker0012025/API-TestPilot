# API-TestPilot 中文 | [English](https://github.com/walker0012025/API-TestPilot/blob/main/EN-README.md)
API-TestPilot，AI驱动的高效接口测试用例生成模型 | AI-Driven Efficient API Test Case Generation Model

### 🌟 API-TestPilot 模型简介

API-TestPilot，中文名**API 试飞员**，是一名Ai生成**接口测试用例**的Ai人工智能模型，旨在利用Ai技术帮助软件测试工程师提升**接口测试**工作效率和跟上Ai时代技术发展要求。

### 🎉 API-TestPilot 模型新闻
- 🎁 2025.04.05 API-TestPilot 1.0 版本正式开源，正式上线。
- 🎁 2025.04.06 API-TestPilot 1.1 版本修复长文本生成重复问题，待上线（预计4月7日上线，在脚本跑内测中）
- 🎁 2025.04.07 API-TestPilot 1.1 修复了长文本生成中的重复问题，现已上线。
- 🎁 2025.04.10 API-TestPilot 1.2 预计4月11日上线。
- 🔥 请不懂尊重人、骂人的白嫖党注意，我没义务免费教你，已经出现这种情况，所以我现在将开源节奏放缓，关注进展的朋友要怪就怪那些不尊重人的白嫖党。
- 🔥 开源的模型只具备生成接口测试用例的能力。想解锁其他大招或者能力，可以联系我学习，教真东西、真落地，目前毕业学员薪资均纯月薪（不算其他）在20K~40K之间。
- 🔥 喜欢本项目，可以点个stars，你的关注是我持续迭代的动力。
### 🚀 API-TestPilot 核心特征

在使用 API-TestPilot 模型时，只需要将接口文档信息给到模型，API-TestPilot 就可以帮你生成对应的接口测试用例。

部署模型简单及需要的硬件成本不大，API-TestPilot 模型**蒸馏和硬件消耗成本380RMB**，经测试推理过程实际**消耗显存20G**左右，可在**Tesla V100 单卡32G显存**的设备流畅运行（未加速），**单卡24G显存**的设备理论可行（未测试）。

API-TestPilot  将从以下几个维度思考和生成对应的接口测试用例：

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404111524_01.png)

### 💡 API-TestPilot 要点提醒

首先 API-TestPilot 模型生成接口测试用例时考虑的场景已经很全了，甚至超过常规接口测试的要求。但是我们没有办法获取公司数据，无法知道你具体的业务流，如果对业务流有严格要求，**解决办法**有：

1、再次训练，训练代价不大。比如 API-TestPilot 模型训练成本380RMB，此费用包含硬件和蒸馏成本。

2、通过框架，具体效果可查看此文档后面的视频。训练和框架这两者都需要测试开发工程师具备一定的技术能力，当然，利用Ai技术给测试提升的工作效率也会带来指数的提升。

3、项目中的调用代码demo仅用于效果评测，如有其他需求，需自行解决。

4、一千个软件测试工程师就有一千个哈姆雷特，所以API-TestPilot 模型的评测及各项评估指标，**_我们更期待你自己亲手实操和体验，后面有详细的实操部署教程。_**

### 👥 API-TestPilot 贡献人员

1、API-TestPilot 是测试开发俊哥和其学员共同完成。API-TestPilot 模型命名由**付佳星**完成，readme英文内容由**周松**完成，模型评测及数据集等工作其他同学**全程参与**、训练及硬件准备部署过程由测试开发俊哥完成。

2、这些同学具备从**蒸馏、清洗、测试模型训练、测试模型评测、测试模型部署**等全过程技术，尤其Ai技术在测试行业的应用，处于行业领先。企业在选择小伙伴时为了避免冒充，如果有验真需求，可通过这些小伙伴联系到测试开发俊哥，测试开发俊哥将提供证明，证明将包含对应小伙伴的操作记录。以下为贡献名单（排名不分先后）。

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404122210.png)

### 📌 API-TestPilot 实操教程

备注：以下教程为单卡环境，单机单卡、多机多卡、CUDA、CUDNN等需自行解决（大多数情况无需解决）。

1、硬件设备：准备一张卡，建议32G显存，24G显存理论可以（未测试）。

2、版本依赖：python版本3.12.4，pip建议23.3.1版本，建议用虚拟环境，非常不建议物理环境。

3、项目下载：请git clone https://github.com/walker0012025/API-TestPilot.git ，下载项目到你的服务器。

4、进入项目：cd API-TestPilot。

5、安装依赖：pip install -r requirements.txt （建议虚拟环境）。

6、下载模型：控制台输入python download_api_testpilot_model.py并执行，下载时间可能较长，请耐心等待下载完毕。

7、修改路径：打开api_testpilot_generate_case.py 源码，将model_path的路径替换为你的实际路径（一般不用改，报错就切换到根目录 find -name api-testpilot-model 查找一下，找着和源码中相似的路径替换）。

8、生成用例：控制台输入python api_testpilot_generate_case.py 执行，开始生成接口测试用例（源码已准备接口信息，可查看源码后自行修改）。

### ⚡ API-TestPilot 结合Ai执行接口测试框架可实现有接口测试用例即可自动执行测试
### ⚡ 框架开发及相关技术可找测试开发俊哥学习，以下为平台根据生成的测试用例自动执行接口测试

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/1743762862000.gif)

### 🙏 来自 API-TestPilot 及测试开发俊哥的致谢 

1、感谢智谱Ai，API-TestPilot   [是基于智谱Ai旗下ZhipuAI/glm-4-9b-chat模型进行训练。](https://github.com/THUDM/GLM-4)

2、感谢deepseek，API-TestPilot [蒸馏来源于她](https://github.com/deepseek-ai/DeepSeek-R1)

3、感谢modelscope魔搭社区提供模型仓库，API-TestPilot [模型文件存储在modelscope魔搭社区仓库上](https://github.com/modelscope)

