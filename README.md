# API-TestPilot 中文 | [English](https://github.com/walker0012025/API-TestPilot/blob/main/EN-README.md)

### 🌟 API-TestPilot 模型简介

API-TestPilot，中文名**API 试飞员**，由测试开发俊哥及其学员共同训练的**AI生成接口测试用例**模型。旨在利用Ai技术提升软件测试工程师接口测试工作效率和帮助测试工程师跟上Ai时代技术发展要求。

### 🍓 API-TestPilot 使用必读
- 🔥 鉴于2023年以来，部分IT技能培训机构的教职员工及销售人员在知识产权和原创内容方面存在不尊重行为，让我不胜其烦，特此明确：本模型不向IT技能类培训机构（包括从事IT技能培训的个人博主）授权。
- 🔥 其他非IT技能培训领域的公司可自由使用本开源模型，无需额外授权。
- 🔥 请不尊重人、甚至骂人的某些要了又要的白嫖同学注意，我没有义务免费教您，请您自重。
- 🔥 我的愿景：提升整个测试行业的技术水平。倘若您喜欢本项目，欢迎给予star支持，您的认可是我持续优化与创新的动力源泉。

### 🎉 API-TestPilot 版本新闻
- 🎁 2025.04.05 API-TestPilot 1.0 版本正式开源，正式上线。
- 🎁 2025.04.06 API-TestPilot 1.1 版本修复长文本生成重复问题，待上线（预计4月7日上线，在脚本跑内测中）
- 🎁 2025.04.07 API-TestPilot 1.1 修复了长文本生成中的重复问题，现已上线。
- 🎁 2025.04.10 API-TestPilot 1.2 预计4月11日上线。解决生成的接口用例，覆盖度可能会出现掉点的问题。
- 🎁 2025.04.11 API-TestPilot 1.2 4月11日上线计划先搁置，因其他事情耽搁，预计一周内上线。
- 🎁 2025.04.13 API-TestPilot 1.2 版本已上线，修复覆盖度可能掉点的问题。

### 🚀 API-TestPilot 核心特征

在使用 API-TestPilot 模型时，只需要将接口文档信息给到模型，API-TestPilot 就可以帮您生成对应的接口测试用例。

部署模型简单及需要的硬件成本不大，API-TestPilot 模型**蒸馏和硬件消耗成本380RMB**，经测试推理过程实际**消耗显存20G**左右，可在**Tesla V100 单卡32G显存**的设备流畅运行，**单卡24G显存**的设备理论可行（已有测试同学在22G的2080TI上成功运行）。

API-TestPilot  将从以下几个维度思考和生成对应的接口测试用例：

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404111524_01.png)

### 💡 API-TestPilot 要点提醒

首先 API-TestPilot 模型生成接口测试用例时考虑的场景已经很全了，甚至超过常规接口测试的要求。但是我没有办法获取公司数据，无法知道您具体的业务流，如果对业务流有严格要求，**解决办法**有：

1、再次训练，训练代价不大。比如 API-TestPilot 模型训练成本380RMB，此费用包含硬件和蒸馏成本。

2、通过框架，具体效果可查看此文档后面的视频。训练和框架这两者都需要测试开发工程师具备一定的技术能力，当然，利用Ai技术给测试提升的工作效率也会带来指数的提升。

3、项目中的调用代码demo仅用于效果评测，如有其他需求，需自行解决。

4、一千个软件测试工程师就有一千个哈姆雷特，所以API-TestPilot 模型的评测及各项评估指标，**_我更期待您自己亲手实操和体验，后面有详细的实操部署教程。_**

### 👥 API-TestPilot 贡献同学

1、API-TestPilot 是测试开发俊哥和其学员共同完成。API-TestPilot 模型命名由**付佳星**完成，readme英文内容由**周松**完成，模型评测及数据集等工作其他同学**全程参与**、训练及硬件准备部署过程由测试开发俊哥完成。

2、这些同学具备从**蒸馏、清洗、测试模型训练、测试模型评测、测试模型部署**等全过程技术，尤其Ai技术在测试行业的应用，处于行业领先。企业在选择小伙伴时为了避免冒充，如果有验真需求，可通过这些小伙伴联系到测试开发俊哥，测试开发俊哥将提供证明，证明将包含对应小伙伴的操作记录。以下为贡献名单（排名不分先后）。

3、其他未能参与本次开源项目的同学，无需担心，后续的版本迭代会让您参与。

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404122210.png)

### 📌 API-TestPilot 实操教程

备注：以下教程为单卡环境，单机单卡、多机多卡、CUDA、CUDNN等需自行解决（大多数情况无需解决）。

1、硬件设备：准备一张卡，建议32G显存，24G显存理论可以（已有测试同学在22G的2080TI上成功运行）。

2、版本依赖：python版本3.12.4，pip建议23.3.1版本。

3、项目下载：请git clone https://github.com/walker0012025/API-TestPilot.git ，下载项目到您的服务器。

4、进入项目：cd API-TestPilot。

5、安装依赖：pip install -r requirements.txt。

6、下载模型：控制台输入python download_api_testpilot_model.py并执行，下载时间可能较长，请耐心等待下载完毕。

7、修改路径：打开api_testpilot_generate_case.py 源码，将model_path的路径替换为您的实际路径（一般不用改，报错就切换到根目录 find -name api-testpilot-model 查找一下，找着和源码中相似的路径替换）。

8、生成用例：控制台输入python api_testpilot_generate_case.py 执行，开始生成接口测试用例（源码已准备接口信息，可查看源码后自行修改）。

### 📝 API-TestPilot开源模型非Ai测试技术核心，仅提供了Ai生成接口测试用例的能力
### 📝 一个开源的模型、框架、工具无法适配所有的公司，只有技术人才，才能适配所有的公司。
### 🎯 如您想进阶Ai测试开发，您将掌握以下内容
- 🎁 Ai测试平台开发（独立开发，前后端分离架构）
- 🎁 Ai生成测试用例（注入企业测试思维，两分钟完成3~5天工作量）
- 🎁 Ai执行接口测试（实现一键化的Ai执行接口测试平台，从接口文档到报告一键化）
- 🎁 Ai执行web/app测试（实现一键化的Ai执行web/app测试平台，全方位提升测试效率）
- 🎁 Ai Checkin 技术 （从源头、代码、单元等维度对项目进行全流程管控）
- 🎁 Ai 模型测试技术 （从模型评测、压测等各种维度实现对模型进行测试）
- 🎁 其他Ai测试技术等

### ⚡ 当您看到类似下图的信息出现时，恭喜你成功了。
### ⚡ Ai测试开发处于红利期，进阶AI测试开发，可以通过社交渠道搜索测试开发俊哥（小红书、抖音、知乎、B站）

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/data_01.PNG)

### 🙏 引用
```bibtex
@misc{glm2024chatglm,
    title={ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools}, 
    author={Team GLM and Aohan Zeng and Bin Xu and Bowen Wang and Chenhui Zhang and Da Yin and Diego Rojas and Guanyu Feng and Hanlin Zhao and Hanyu Lai and Hao Yu and Hongning Wang and Jiadai Sun and Jiajie Zhang and Jiale Cheng and Jiayi Gui and Jie Tang and Jing Zhang and Juanzi Li and Lei Zhao and Lindong Wu and Lucen Zhong and Mingdao Liu and Minlie Huang and Peng Zhang and Qinkai Zheng and Rui Lu and Shuaiqi Duan and Shudan Zhang and Shulin Cao and Shuxun Yang and Weng Lam Tam and Wenyi Zhao and Xiao Liu and Xiao Xia and Xiaohan Zhang and Xiaotao Gu and Xin Lv and Xinghan Liu and Xinyi Liu and Xinyue Yang and Xixuan Song and Xunkai Zhang and Yifan An and Yifan Xu and Yilin Niu and Yuantao Yang and Yueyan Li and Yushi Bai and Yuxiao Dong and Zehan Qi and Zhaoyu Wang and Zhen Yang and Zhengxiao Du and Zhenyu Hou and Zihan Wang},
    year={2024},
    eprint={2406.12793},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
