# API-TestPilot
API-TestPilot，AI-Driven Efficient API Test Case Generation Model

### 🌟 Overview of API-TestPilot

API-TestPilot is an AI-powered model designed to generate API test cases automatically. It aims to empower software testing engineers to enhance API testing efficiency and align with AI-driven technological advancements. (Commercial use is permitted. Please cite API-TestPilot when referencing. This is an open-source project; the author assumes no liability.)

### 🚀 API-TestPilot Core Features

By providing API documentation to the model, API-TestPilot generates comprehensive test cases tailored to your API specifications.

Deployment Simplicity & Hardware Requirements
Cost-Efficient Training: Total distillation and hardware costs amount to 380 RMB.
Hardware Compatibility:
Smooth operation on Tesla V100 (32GB VRAM).
Theoretically compatible with 24GB VRAM GPUs (untested).

API-TestPilot evaluates and generates test cases across the following dimensions:

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404111524_01.png)

### 💡 API-TestPilot Key Notes

Comprehensive Coverage: The model generates test cases exceeding conventional requirements but may lack domain-specific business logic. Solutions:

1.Fine-tuning: Low-cost retraining (estimated 380 RMB for hardware and distillation).

2.Framework Integration: Custom logic integration via testing frameworks (see demo video below).

3.Repetition in Long Inputs: Occasional redundant outputs may occur with lengthy API documentation (to be resolved in future versions).

4.Speed Optimization: The provided demo code focuses on functionality; inference acceleration (2-10s latency) requires custom implementation.

5.Subjective Evaluation: Testing practices vary; hands-on evaluation is strongly recommended.


### 👥 API-TestPilot Contributors

1.API-TestPilot was completed jointly by Brother Jun and his partners. The API-TestPilot model was named by ** Fu Jiaxing **. Other students ** participated in the entire process of model evaluation and data sets **. The training and hardware preparation and deployment process are completed by the test and development brother.

2.These little friends have distilled from **. cleaning. Test model training. Test model evaluation. Full-process technologies such as test model deployment **, especially the application of Ai technology in the testing industry, are leading the industry. In order to avoid impersonation when selecting small partners, if there is a need for authenticity verification, companies can contact the test and development brother through these small partners. The test and development brother will provide a certificate, which will include the operation records of the corresponding small partners. The following is a list of contributions (in no particular order).

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/20250404122210.png)

### 📌 API-TestPilot Deployment Guide

Environment Setup

1.Hardware: Single GPU (32GB VRAM recommended; 24GB VRAM untested).

2.Dependencies:Python 3.12.4, pip 23.3.1 (use virtual environments).

3.Clone Repository:
git clone https://github.com/walker0012025/API-TestPilot.git  

4.cd API-TestPilot  

5.Install Dependencies:pip install -r requirements.txt。

6.Path Configuration: Modify model_path in api_testpilot_generate_case.py if necessary (use find -name api-testpilot-model to locate the model).

7.Modify the path: Open the api_testpilot_generate_case.py source code and replace the path of model_path with your actual path (generally, you don't need to change it. If you report an error, switch to the root directory find -name api-testpilot-model and find a path similar to that in the source code to replace it).

8.Generate Test Cases:python api_testpilot_generate_case.py ,start generating interface test cases (interface information has been prepared in the source code, you can view the source code and modify it yourself).

### ⚡ API-TestPilot combined with Ai execution interface testing framework enables automatic testing with interface test cases
### ⚡ Framework development and related technologies can be learned from test developer Jun Ge. The following is the platform automatically executes interface testing based on the generated test cases.

![Image](https://github.com/walker0012025/API-TestPilot/blob/main/data/1743762862000.gif)

### 🙏 Thanks from API-TestPilot and Brother Jun of Test Development

1.Thank to Zhipu AI，API-TestPilot   [The training is based on the ZhipuAI/glm-4- 9b-chat model owned by Intelligent Intelligence Ai.](https://github.com/THUDM/GLM-4)

2.Thank to deepseek，API-TestPilot [Distillation comes from it](https://github.com/deepseek-ai/DeepSeek-R1)

3.Thank to modelscope，API-TestPilot [Model files are stored on the modelscope community repository](https://github.com/modelscope)

